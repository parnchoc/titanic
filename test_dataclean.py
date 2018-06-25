#!/usr/bin/env python
import numpy as np 
import pandas as pd 

#file name
Test = 'test.csv'
Train = 'train.csv'

#read data from .csv file
dtype = {'PassengerId':np.str, 'Pclass':np.int32, 'Name':np.str, 'Sex':np.str, 'Age':np.float, 'SibSp':np.int, 'Parch':np.int, \
		'Ticket':np.str, 'Fare':np.float, 'Cabin':np.str, 'Embarked':np.str}
test_df = pd.read_csv(Test, dtype=dtype)
train_df = pd.read_csv(Train, dtype=dtype)

#print original test.csv
print('-----test.csv-----')
print(test_df.head(5))

#print original train.csv
print('-----train.csv-----')
print(train_df.head(5))

#data cleansing
test_df.drop_duplicates(inplace=True)
test_df['Last Name'], test_df['First Name'] = test_df['Name'].str.split(',', 1).str

#write data to test_clean.csv
test_df.to_csv('test_processed.csv', encoding='UTF-8', index=False) 

#print processed test.csv
print('-----test_processed.csv-----')
print(test_df.head(5))