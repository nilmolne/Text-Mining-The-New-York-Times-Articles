# Text-Mining-The-New-York-Times-Articles
This project covers step-by-step how to mine text from The New York Times by using Python

## 

## Application Example

The purpose of this example is to demonstrate the value economists may gain from a more conscious application of text mining techniques by means of an example based on tracking the Greek government-debt crisis crisis of this last decade.

First, we input a time range from 2004 to 2015, to make sure our analysis spans events of interest. Second, the algorithm retrieves only articles published by The New York Times tagged as being geolocated in Greece. Furthermore, only articles labeled as news were taken into account. Articles falling into the category of blog or brief were filtered out prior to the pre-processing stage. Third, our dictionary consisted of: ‘Financial Crisis’, ‘Economic Recession’, and ‘Bank Run’, as we thought it would be a representative dictionary of the events we are looking to track. In addition, as an economic indicator to compare our results with, the 10Y Greek Government Bond Yield was selected.

Given this scenario, the algorithm went through 710 articles, totaling 598,275 words, of which only 3,816 were counted towards occurrences from our dictionary. The normalized frequency of occurrence was calculated as described in section 2.4. Later on, all calculated frequencies within a month, for the 144 months of interest, were summed to give an added normalized frequency of occurrence on a monthly basis.

The results are presented in Figures 1, 2, 3 and 4. Figure 1 and Figure 2 plot the resulting key word frequencies of the article analysis in a given period of time. Comments were added across the graphs as when the algorithm found a frequency over 10% in a given month, an associated meaningful event of the debt crisis had occurred, including: government debt downgrades or write-offs, bailout executions and capital control impositions.

On Figure 3, the same results as in Figure 1 and 2 are plotted but in a single graph and without the added comments. The amount of monthly published articles is also put on a secondary axis. Two things can be observed. On one hand, the amount of articles labeled as geolocated in Greece by The New York Times continuously increased from 2004 to 2015. This suggests that the normalized frequency of occurrence might have to be further normalized by the amount of articles analyzed each month. On the other hand, by means of correlation calculations, we see that in the period from 2008 to 2015, the number of articles analyzed explains the frequency of occurrence well, as opposed to the period ranging from 2004 to 2007. This shows the rational tendency of the media to publish a greater proportion of articles related to a single specific topic when a country is undergoing a crisis.

Finally, on Figure 4, the 10Y Government Bond Yields is plotted along the normalized frequency of occurrence. Using the correlation as a measure of similarity between both time series, we can see that they move similarly as the correlation is found to be 0.5027. If, in addition, we normalize the frequency of occurrence by the amount of monthly articles published, the correlation gets slightly better and accounts for 0.5698. **If correlation is calculated for the time range from 2008 to 2015, it reaches 0.8628 showing that the words in the dicctionary have a significant explanatory power over the Greek government-debt crisis of this last lustrum.**

## Conclusions about the Application

This application shows how text mining can add value to economic research by means of a dictionary text mining technique. Nevertheless, this technique is only a deductive approach in that it starts with a predefined list of words, motivated by a general theory as to why these words matter. The strengths of this approach are simplicity and scalability. Code for its implementation is typically simple, and can be applied easily to massive text files. However, the weakness of this approach is its focus only on words pre-judged by the researcher to be informative while ignoring all other words.

Some other more advanced approaches not discussed in this work like Latent Semantic Analysis, Latent Dirichlet Allocation and Descending Hierarchical Classification look for thematic patterns in a particular corpus without claiming that these patterns hold in other documents. The main strength of these techniques is that they analyze all words within the corpus and yield more sophisticated statistical outputs. Their main disadvantage is programming complexity.
