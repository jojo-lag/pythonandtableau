# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 17:23:23 2022

@author: SINMI OJOLO
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Method 1; to read a json file
json_file = open('loan_data_json.json')
data = json.load(json_file)

# Method 2; to read a json file
with open('loan_data_json.json') as json_file:
    data = json.load(json_file)
    

# Transforming the data to dataframe
loandata = pd.DataFrame(data)

# Lisiting unique values in a column
loandata['purpose']. unique()

# Describing the dataset
loandata.describe()

# Describing data for a specific column
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

# To install numpy; anaconda prompt, write pip install numpy
# Numpy will be used to change log to exp

# Changing the log.annual.inc to exp to get the annual income
income = np.exp(loandata['log.annual.inc'])
loandata['annual income'] = income

# Using IF statement to make decisons for the fico
a= 14
b= 500

if b > a:
    print('b is greater than a')

# Adding more conditions
a= 40
b= 500
c= 1000
if b > a and a < c:
    print('b is greater than a but less than c')
    
# When a condition is not met
a = 40
b = 500
c = 20
if b > a and b < c:
    print('b is greater than a but less than c')
else:
    print('No conditions met')
    
# Another condition different metrics
a = 40
b = 500
c = 30
if b > a and b < c:
    print('b is greater than a but less than c')
elif b > a and b > c:
    print('b is greater than a and c')
else:
    print('No conditions met')
    
    
# Using OR statement
a = 40
b = 500
c = 30
if b > a or b < c:
    print('b is greater than a or less than c')
else:
    print('No conditions met')

# FICO score condition

fico = 500
# fico >= 300 and < 400:'Very Poor'
# fico >= 400 and ficoscore < 600:'Poor'
# fico >= 601 and ficoscore < 660:'Fair'
# fico >= 660 and ficoscore < 780:'Good'
# fico >=780:'Excellent'

if fico >= 300 and fico < 400:
    ficocat = 'Very Poor'
elif fico >= 400 and fico < 600:
    ficocat = 'Poor'
elif fico >= 601 and fico < 660:
    ficocat = 'Fair'
elif fico >= 660 and fico < 700:
    ficocat = 'Good'
elif fico >= 700:
    ficocat = 'Excellent'
else:
    fico = 'Unknown'
print(ficocat)

# Working with loops

fruits = ['apple', 'pear', 'banana', 'cherry']

for x in fruits:
    print(x)
    y= x + '  fruits'
    print(y)
    
for x in range(0, 4):
    y= fruits[x] + ' for sale'
    print(y)
    
# Applying loops to loan data

# Using first ten

length = len(loandata)
ficocat = []
for x in range(0,length):
    category = loandata['fico'][x]
    
    try: 
        if category >= 300 and category < 400:
            cat = 'Very Poor'
        elif category >= 400 and category < 600:
            cat = 'Poor'
        elif category >= 601 and category < 660:
            cat = 'Fair'
        elif category >= 660 and category < 700:
            cat = 'Good'
        elif category >= 700:
            cat = 'Excellent'
        else:
            cat = 'Unknown'
    except:
        cat = 'Unknown'
        
    ficocat.append(cat)

# Recall that series is a column in a data frame, hence converting ficocat from list to series

ficocat = pd.Series(ficocat)
loandata['fico.category'] = ficocat

# df.loc as conditional statement
# df.loc[df[column name] condition, new column name] ='value if the condition is met'

# for interest rates, a new coulmn is wanted; if rate is > 0.12, then high else low

loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'high'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] = 'low'

# No of loans/rows by fico.category

catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color = 'green', width = 0.1)
plt.show()

purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar(color = 'red', width = 0.2)
plt.show()

# scatter plots

ypoint = loandata['annual income']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint, color = '#4acf50')
plt.show()

# Writing to csv
loandata.to_csv('loan_cleaned.csv', index = True)

