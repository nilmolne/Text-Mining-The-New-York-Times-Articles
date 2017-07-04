#############
# Libraries #
#############

import numpy as np
import pandas as pd
import time
from nytimesarticle import articleAPI
import re
from nltk import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from nltk import FreqDist
import requests
from bs4 import BeautifulSoup




##############
# Functions #
#############

def parse_articles(articles):
    
    news = []
    
    for i in articles['response']['docs']:
        
        dic = {}
        dic['date'] = i['pub_date'][0:10] # cutting time of day.
        dic['atype'] = i['type_of_material']
        dic['url'] = i['web_url']
        dic['word_count'] = int(i['word_count'])
        news.append(dic)
        
    return news




def get_articles_url(api, country, start_year, end_year):
    
    all_articles = []
    year = start_year
    
    print('Retrieving articles URL...'),
    
    #Loop through all years of interest
    while year <= end_year:
        
        # Some pages might return a 'No JSON object could be decoded'
        # Example: country = Turkey, year = 1998, page 4
        # To keep this error from stopping the loop a try/except was used.
        for i in range(0,100):

            try:
                # Call API method with the parameters discussed on the README file
                articles = api.search(
                    fq = {'source':['The New York Times'], 
                          'glocations':(country), 
                          'news_desk':('Foreign')}, 
                    begin_date = str(year) + '0101', 
                    end_date = str(year) + '1231', 
                    sort = 'oldest', page = str(i))
                
                # Check if page is empty
                if articles['response']['docs'] == []: break
                
                articles = parse_articles(articles)
                all_articles = all_articles + articles
                
            except Exception:

                pass
            
            # Avoid overwhelming the API
            time.sleep(1)
            
        year += 1
    
    # Copy all articles on the list to a Pandas dataframe
    articles_df = pd.DataFrame(all_articles)
    
    # Make sure we filter out non-news articles and remove 'atype' column
    articles_df = articles_df.drop(articles_df[articles_df.atype != 'News'].index)
    articles_df.drop('atype', axis = 1, inplace = True)
    
    # Discard non-working links (their number of word_count is 0).
    # Example: http://www.nytimes.com/2001/11/06/world/4-die-during-police-raid-in-istanbul.html
    articles_df = articles_df[articles_df.word_count != 0]
    articles_df = articles_df.reset_index(drop = True)
    
    print('Done!')
    
    return(articles_df)




def scarp_articles_text(articles_df):
    
    # Unable false positive warning from Pandas dataframe manipulation
    pd.options.mode.chained_assignment = None
    
    articles_df['article_text'] = 'NaN'
    session = requests.Session()
    
    print('Scarping articles body text...'),
    
    for j in range(0, len(articles_df)):
        
        url = articles_df['url'][j]
        req = session.get(url)
        soup = BeautifulSoup(req.text, 'lxml')

        # Get only HTLM tags with article content
        # Articles through 1986 are found under different p tag 
        paragraph_tags = soup.find_all('p', class_= 'story-body-text story-content')
        if paragraph_tags == []:
            paragraph_tags = soup.find_all('p', itemprop = 'articleBody')

        # Put together all text from HTML p tags
        article = ''
        for p in paragraph_tags:
            article = article + ' ' + p.get_text()

        # Clean article replacing unicode characters
        article = article.replace(u'\u2018', u"'").replace(u'\u2019', u"'").replace(u'\u201c', u'"').replace(u'\u201d', u'"')

        # Copy article's content to the dataframe
        articles_df['article_text'][j] = article
    
    print('Done!')
    
    return articles_df




def tokenize(text):
    
    # Convert to lower case
    words = map(lambda word: word.lower(), word_tokenize(text))
    
    # Remove stop words
    cachedStopWords = stopwords.words("english")
    words = [word for word in words
                  if word not in cachedStopWords]
    
    # Steam the words
    tokens =(list(map(lambda token: PorterStemmer().stem(token), words)))
    
    # Remove non-letters 
    p = re.compile('[a-zA-Z]+')
    
    # Remove less than 3 length words
    min_length = 3
    filtered_tokens = list(filter(lambda token: p.match(token) and len(token) >= min_length, tokens))
    
    return filtered_tokens




def text_mine_articles(articles_df, bag_of_words):
    
    #articles_df = articles_df.drop(articles_df[articles_df.word_count == 0].index) # 1991 art 21 prevensio
    #articles_df = articles_df.reset_index(drop = True)
    
    bag_of_words = tokenize(bag_of_words)
    articles_df['num_occurr'] = 0
    
    # 'Set' to make the counting operation faster
    set_of_words = set(bag_of_words)
    
    print('Text mine articles...'),
    
    for j in range(0, len(articles_df)):
        
        # Convert article body into a list of tokens
        tokenized_article = tokenize(articles_df['article_text'][j])
        
        # Count occurrences of the dictionary of words
        occurrences = [word for word in tokenized_article
                        if word in set_of_words]
        
        # Copy amount of occurrences found to the dataframe
        amount = len(occurrences)
        articles_df['num_occurr'][j] = amount
        
    # Compute frequency of occurrence found in each article dividing
    # the amount of words counted as occurrences by the amount of words in the article
    articles_df['freq_occurr'] = articles_df['num_occurr']/articles_df['word_count']   
   
    print('Done!')
 
    return articles_df




def get_monthly_results(articles_df, start_year, end_year):
    
    print('Arranging results monthly into a new dataframe...'),
    
    # Number of months in range of analysis
    range = 12*(end_year - start_year + 1)
    
    # Prepare timeseries dataframe for displaying results
    columns = ['month_freq_occurr', 'num_articles','norm_freq_occurr']
    results_df = pd.DataFrame(columns = columns)
    results_df['date'] = pd.date_range(str(start_year) + '-01', periods = range, freq = 'M')
    
    # Set date as index to move data from articles_df to results_df conviniently
    results_df = results_df.set_index(['date'])
    results_df = results_df.fillna(0.0) # with 0s rather than NaNs
    
    # Display results on a monthly basis
    i = 0
    while i < len(articles_df):
        
        # Cut day from date column
        date = articles_df['date'][i][0:7] 
        
        # Group numbers monthly by summing daily results
        results_df.loc[date]['num_articles'] += 1
        results_df.loc[date]['month_freq_occurr'] += articles_df['freq_occurr'][i]
        
        i += 1
    
    # Normalize the monthly added frequency of occurrences by the amount of articles published in that month
    results_df['norm_freq_occurr'] = results_df['month_freq_occurr']/results_df['num_articles']
    
    # Detele the NaN divisions if any
    results_df['norm_freq_occurr'][results_df['norm_freq_occurr'].isnull()] = 0.0
    
    print('Done!')
    
    return results_df




def visualize_results(results_df, country, start_year, end_year, dictionary):
    
    # Print on Jupyter Notebook
    get_ipython().magic(u'matplotlib inline')
    
    # Define plot properties
    plot_title = 'Results for Dictionary: "' + dictionary + '" in ' + country + ' from Jan ' + str(start_year) + ' to Dec ' + str(end_year)
    results_df.norm_freq_occurr.plot(legend = True, label = 'Monthly Normalized Frequency of Occurrence', 
                                        figsize = (15, 5), title = plot_title)
    results_df.num_articles.plot(secondary_y = True, style = 'g',
                                    label = 'Articles Published', legend = True)

