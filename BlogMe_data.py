# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 22:18:16 2022

@author: SINMI OJOLO
"""

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# reading excel or xlsx files
data = pd.read_excel('articles.xlsx')

# Summary of the data
data.describe()

# Summary of the columns
data.info()

# Counting the number of articles per source
# Format og groupby: df.groupby(['column_to_groupby'])['column_to_count'].count()

data.groupby(['source_id'])['article_id'].count()

# No of reactions by publisher
data.groupby(['source_id'])['engagement_reaction_count'].sum()

# Dropping columns
data = data.drop('engagement_comment_plugin_count' , axis = 1)

# Functions in python

def thisFunction():
    print('this is my First Function!')
    
thisFunction()

# This is a function with variables

def aboutMe(name, surname, location, bestfood):
    print('This is '+name+' My surname is '+surname+' I am from '+location+' I love '+bestfood)
    return name, surname, location, bestfood
    

a= aboutMe('Jojo', 'Ojolo', 'Nigeria', 'Garri')

# Usinf for loops in functions

def favfood(food):
    for x in food:
        print('Top food is'+x)
    
    
fastfood = ['burger', 'pizza', 'pie']

favfood(fastfood)

# Creating a keyword flag

keyword = 'crash'

# Creating a for loop to isoalte each title row


# length = len(data)
# keyword_flag = []
# for x in range(0, length):
#     heading = data['title'][x]
#     if keyword in heading:
#         flag = 1
#     else:
#         flag = 0
#     keyword_flag.append(flag)
    
# Creating a function

def keywordflag(keyword):
    
    length = len(data)
    keyword_flag = []
    for x in range(0, length):
        heading = data['title'][x]
        try:
            if keyword in heading:
                flag = 1
            else:
                flag = 0
        except:
            flag = 0
        keyword_flag.append(flag)
    return keyword_flag
    
    
keywordflag = keywordflag('murder')

# Creating a new column in the dataframe

data['keyword_flag'] = pd.Series(keywordflag)

# SentimentIntensityAnalyzer

sent_int = SentimentIntensityAnalyzer()

text = data['title'][16]
sent = sent_int.polarity_scores(text)
neg = sent['neg']
pos = sent['pos']
neu = sent['neu']

# Adding a for loops to extract sentiment per title
title_neg_sentiment = []
title_pos_sentiment = []
title_neu_sentiment = []

length = len(data)

for x in range(0, length):
    try:
        text = data['title'][x]
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(text)
        neg = sent['neg']
        pos = sent['pos']
        neu = sent['neu']
    except:
        neg = 0
        pos = 0
        neu = 0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)

title_neg_sentiment = pd.Series(title_neg_sentiment)
title_pos_sentiment = pd.Series(title_pos_sentiment)
title_neu_sentiment = pd.Series(title_neu_sentiment)

data['title_neg_sentiment'] = title_neg_sentiment
data['title_pos_sentiment'] = title_pos_sentiment
data['title_neu_sentiment'] = title_neu_sentiment

# Writing the data

data.to_excel('blogme_cleaned.xlsx', sheet_name = 'blogmedata', index = False)