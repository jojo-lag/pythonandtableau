# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 18:25:49 2022

@author: SINMI OJOLO
"""

# Code to import pandas

import pandas as pd

# file_name = pd.read_csv('file.csv') <----- code format of read_csv

data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv', sep=';')

# Summary of the data

data.info()

# Working with calculations

# Defining variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberofItemPurchased = 6 

# Mathematical Operations on Python

ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberofItemPurchased * ProfitPerItem
CostPerTransaction = NumberofItemPurchased * CostPerItem
SellingPricePerTransaction = NumberofItemPurchased * SellingPricePerItem

# CostPerTransaction Column Calculation

# CostPerTransaction = NumberofItemPurchased * CostPerItem
# variable = dataframe['column_name']

data.info()
CostPerItem = data['CostPerItem']
NumberofItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction =  CostPerItem * NumberofItemsPurchased

# Creating a column for CostPerTransaction in the data frame

data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased'] 

# SalesPerTransaction coulmn created in the data frame

SellingPricePerItem = data['SellingPricePerItem']
NumberofItemsPurchased = data['NumberOfItemsPurchased']
SalesPerTransaction =  SellingPricePerItem * NumberofItemsPurchased

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

# ProfitPerTranscation column created in the data frame = sales - cost

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

# MarkupPerTransaction column created in the data frame = (sales - cost)/cost

data['ProfitPerTransaction'] = ProfitPerTransaction
data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction'] )/data['CostPerTransaction']
data['Markup'] =  (data['ProfitPerTransaction'] )/ data['CostPerTransaction']

# Rounding up to the nearest whole number

roundmarkup = round(data['Markup'], 2)

data['Markup'] = round(data['Markup'], 2)

# Merging the year, month and date columns

# Check the data types

print(data['Day']. dtype)

# Changing data type

day = data['Day'].astype(str)
year = data['Year'].astype(str)
print(year. dtype)


print(day. dtype)
my_date = day + "/" + data['Month'] + "/" + year

data['Date'] = my_date

# Using iloc to view specific columns/rows

data.iloc[0] # views the row with index = 0
data.iloc[0:3] # views the first three rows
data.iloc[-5:] # views last five rows

data.head(5) # brings in first five rows
data.iloc[:,2] # brings in the second column

# Splitting the three keywords in the customer's keyword column
# new_var = column. str.split(','expand = True) 
split_col = data['ClientKeywords']. str.split(',' , expand= True)

# Creating columns for the split column of the client keyword column
data['Client age'] = split_col[0]
data['Client Type'] = split_col[1]
data['LengthOfContract'] = split_col[2]

# Using the replace function to remove the bracket 

data['Client age'] = data['Client age']. str. replace('[', '')
data['LengthOfContract'] = data['LengthOfContract']. str.replace(']', '')

# Using the lower function to change the sentence to lowercase

data['ItemDescription'] = data['ItemDescription']. str. lower()

# Merging or Combining one or more datasets

# Bringing in a new datasets

seasons = pd.read_csv('value_inc_seasons.csv', sep = ';')

# Merging files to the same data frame: megred_df = pd.merge(df_old, df_new,on = 'key')

data = pd.merge(data, seasons, on = 'Month')

# Removing columns from the data frame

# df = df.drop('columnname', axis = 1)

data = data.drop('ClientKeywords', axis = 1)
data = data.drop('Day', axis = 1)

# Removing multiple columns at the same time
data = data.drop(['Year', 'Month'], axis = 1)

# Exporting into a CSV file

data.to_csv('ValueInc_Cleaned.csv', index = False)

