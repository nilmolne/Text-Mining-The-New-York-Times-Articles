# Text-Mining-The-New-York-Times-Articles

This project covers step-by-step how to **mine text from The New York Times' online articles by using Python given a dictionary of words, time range and country of interest**. At the same time, it enumerates the key steps to follow in any text mining project, and gives an overview of a specific dictionary text mining technique. The intuition behind this technique is that the frequency of words and their occurrence are good indicators of the topic or sentiment expressed in texts.

## Introduction 

The code is structured in six stages as shown in the figure below. The approach to each stage is briefly explained along this Readme file.

<p align="center">
  <img src = "Algorithm.png" height = "75%" width = "75%">
</p>

## 1 Building the Article Database

To begin analyzing text, one must build a collection of documents (or a corpus in data mining argot). The documents to analyze could be taken from news articles, financial contracts, social media, or written reports of various kinds. In our case the corpus is going to be a set of online articles from The New York Times.

The New York Times offers developers up to 11 search APIs to retrieve certain information for different uses. For our purposes, the Article Search API will be the one used. All the programmer needs to do to access it is to request an API key, which is given almost instantaneously, and install the nytimesarticle package in your Python environment, which is wrapper to query the New York Times Article Search API.

With the Article Search API, one can search New York Times articles from Sept. 18, 1851 to today, retrieving the URL to the articles, plus their headlines, abstracts, lead paragraphs, associated multimedia, and other article metadata. Note that the API does not return full raw text of articles but rather returns the article URLs. These URLs can conceivably be used to scrape the full text of the articles of interest, on a later stage.

*The API key can be requested at: http://developer.nytimes.com/signup*

*The nytimesarticle package can be downloaded from: https://pypi.python.org/pypi/nytimesarticle/0.1.0*

## 2 Scarping Article Content

Given the corpus of articles we want to analyze; we have to retrieve their content one by one. The goal is to extract each article raw text to be able to pre-process it. However, each article online is a webpage coded in HTML language of which, so far, we only have got its URL.

HTML language provides a means to create structured documents by denoting structural semantics for text such as headings, paragraphs, lists, links, quotes and other items. HTML elements are delineated by tags, written using angle brackets. Browsers do not display the HTML tags, but use them to interpret the content of the page.

Analyzing many online articles from The New York Times, we found out how their developers structure their HTML code. Article text, the content of an article webpage we are looking forward to scarping within many other text data, is either found under **p tags of class “story-body-text story-content”** or in earlier published articles under **p tags with an itemprop called “articleBody”**. Headliners, commercials, and others are stored in different tags.

This project uses BeautifulSoup for pulling data out of the HTML pages. As a result, for each article, we get a string of text including all their paragraphs ready to be pre-processed.

## 3 Analytical Article Pre-processing

Once the corpus is specified, and we have the raw text of each article, the next step is to transform it into a format amenable to analysis. In other words, we want to break each article raw text into tokens. Tokenize involves representing text as a list of words, numbers, punctuation, and potentially other symbols like currency markers, which will become the input for further processing. The result of a tokenization of an article is the so-called bag of words.

A key aspect of text mining is to reduce the dimensionality of bag of words representations to eliminate ‘noise’ to highlight only the articles’ distinctive content. There are a number of techniques available to deal with words that are superfluous to the content of the corpus. The more important are listed below:

1.	Remove punctuation and rare words: ‘In’, ‘at’, ‘the, ‘a’ … are extremely common words but contribute little to distinguishing the content of one article from the content of another. So these so-called stop-words are often dropped from the bag.

2.	Stemming: In practice, it translates to cutting off affixes and counting just stems. For example, the word ‘censoring’ contains the stem ‘censor’ and the affix ‘-ing’. Therefore, ‘censoring’ and ‘censor’ once stemmed would be treated as two instances of the same token.

3.	Case folding: It involves converting all alphabetic tokens to lowercase. In some cases, though, this might change meaning for some nouns. For example, an acronym such as ‘US’ (referring to the United States) is erroneously converted to the pronoun ‘us’.

To tokenize the articles’ string of words, remove punctuation, steam and case fold the bag of words, we use a suite of libraries and programs for symbolic and statistical natural language processing called Natural Language Toolkit (or more commonly NLTK).

## 4 Text Mining the Articles

To text mine the article this project uses 

## 5 Time Series for Dictionary Occurrence

Canviar Nom d'aquesta seccio al diagrama.

## 6 Visualizing the Results

## An Application in Economic Research

Finally, if you are curious about how can this algorithm be used in Economic Research, take a look at the application proposed in the repository or **click here**.

Enjoy!

