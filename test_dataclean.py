#!/usr/bin/env python
import numpy as np 
import pandas as pd 

#read data from test.csv
df = pd.read_csv('test.csv')
print('-----test.csv-----')
print(df.head(3))

df['Last Name'], df['First Name'] = df['Name'].str.split(',', 1).str

#write data to test_clean.csv
df.to_csv('test_processed.csv', encoding='UTF-8', index=False) 
print('-----test_processed.csv-----')
print(df)
print(df.head(3))