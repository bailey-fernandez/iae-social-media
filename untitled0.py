# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1d8iqWUSLiIx1Yn-9eKHbMgbLKiuCxxhj
"""

pip install github

pip install git+https://github.com/JustAnotherArchivist/snscrape.git

import snscrape as sntwitter
import pandas as pd 

# Creating list to append tweet data to
tweets_list2 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('International Art English since:2007-01-01 until:2023-01-01').get_items()):
    if i>5000:
        break
    tweets_list2.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
    
# Creating a dataframe from the tweets list above
tweets_df2 = pd.DataFrame(tweets_list2, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

pip install snscrape

import snscrape.modules.twitter as sntwitter
import pandas as pd

tweets = []

for number_of_tweet, tweet in enumerate(sntwitter.TwitterSearchScraper("International Art English").get_items()):
    if number_of_tweet > 5000:
        break
    tweets.append([tweet.date, tweet.content])

tweets_sheets = pd.DataFrame(tweets, columns=["Date", "Content"])

print(tweets_sheets)

import snscrape.modules.twitter as sntwitter
import pandas as pd

tweets = []

for number_of_tweet, tweet in enumerate(sntwitter.TwitterSearchScraper("space").get_items()):
  if number_of_tweet > 10000:
    break
  tweets.append([tweet.date, tweet.content])

for number_of_tweet, tweet in enumerate(sntwitter.TwitterSearchScraper("parallelism").get_items()):
    if number_of_tweet > 10000:
        break
    tweets.append([tweet.date, tweet.content])

for number_of_tweet, tweet in enumerate(sntwitter.TwitterSearchScraper("involution").get_items()):
    if number_of_tweet > 10000:
        break
    tweets.append([tweet.date, tweet.content])

for number_of_tweet, tweet in enumerate(sntwitter.TwitterSearchScraper("biopolitical").get_items()):
    if number_of_tweet > 10000:
        break
    tweets.append([tweet.date, tweet.content])

for number_of_tweet, tweet in enumerate(sntwitter.TwitterSearchScraper("transversal").get_items()):
    if number_of_tweet > 10000:
        break
    tweets.append([tweet.date, tweet.content])


tweets_sheets = pd.DataFrame(tweets, columns=["Date", "Content"])

print(tweets_sheets)

import snscrape.modules.twitter as sntwitter
import pandas as pd

tweets = []

for number_of_tweet, tweet in enumerate(sntwitter.TwitterSearchScraper("space, Art").get_items()):
    if number_of_tweet > 10000:
        break
    tweets.append([tweet.date, tweet.content])

for number_of_tweet, tweet in enumerate(sntwitter.TwitterSearchScraper("parallelism, Art").get_items()):
    if number_of_tweet > 10000:
        break
    tweets.append([tweet.date, tweet.content])

for number_of_tweet, tweet in enumerate(sntwitter.TwitterSearchScraper("involution, Art").get_items()):
    if number_of_tweet > 10000:
        break
    tweets.append([tweet.date, tweet.content])

for number_of_tweet, tweet in enumerate(sntwitter.TwitterSearchScraper("biopolitical, Art").get_items()):
    if number_of_tweet > 10000:
        break
    tweets.append([tweet.date, tweet.content])

for number_of_tweet, tweet in enumerate(sntwitter.TwitterSearchScraper("transversal, Art").get_items()):
    if number_of_tweet > 10000:
        break
    tweets.append([tweet.date, tweet.content])

tweets_sheets = pd.DataFrame(tweets, columns=["Date", "Content"])

print(tweets_sheets)