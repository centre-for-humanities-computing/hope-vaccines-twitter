# Explaining the folder and file structure of the repository

As the README.MD is a report on the latest vaccines discourse on the Danish Twitter, this file explains what is going on in the different folders and files.

## Folders

### fig
fig folder contains all the figures which are saved from the Jupyter Notebooks. Most of the figures are shown in the README as part of the report.

### src
The src folder contains a python script ``sentida_afinn_sentiment_score.py`` which takes the vaccines data file and appends Afinn sentiment scores on it. This is to analyze whether the Danish Vader agrees with Afinn sentiment scores. It is not used for more than a sanity check.

## Jupyter Notebooks
There are three Jupyter Notebooks in the root folder.

### explore-vaccines.ipynb
This notebook contains code and figures for all of the vaccines mentions in the Danish Twitter.

1. Counts of mentions per day over time
2. Most popular hashtags
3. Most frequent words (barplot and word cloud)
4. Bigram analysis of co-occurring words

### sentiment-analysis-and-entropy.ipynb
This notebook contains the codes for conducting sentiment analysis on all vaccines mentions in the Danish Twitter alongside with extra sanity checks.

1. Comparison of Afinn sentiment scores to Danish Vader
2. Overall sentiment over time together with count of mentions
3. Sentiment and entropy over time
4. Extra checks: sentiment over time vs mentions, entropy vs mentions, boxplots of average sentiment per month, R squared calculations of Afinn fit to Danish Vader scores

### explore-vaccine-types.ipynb
This notebook contains codes for the different vaccine types.

1. Mentions of AstraZeneca, Moderna, Pfizer over time
2. Sentiment analysis of AstraZeneca and Pfizer