# Gathering data (csv files)
# csv   
# Json/SQL
# Fetch API
# Webscraping

# 1. csv  (coma seperated values)
import pandas as pd
data = pd.read_csv(r'C:\Users\rajku\anagrams.csv')
print(data)

# csv from URL
'''import requests
from io import StringIO
url = ""
header = {"whatever the url we can paste here"}
req = requests.get(url,headers=header)
data = StringIO(req.text)

pd.read_csv(data)'''

# sep perameter
# data = pd.read_csv("collge.tsv", sep='\t')      # tsv means tab seperated values

#Changing names of columns 
data = pd.read_csv(r'C:\Users\rajku\anagrams.csv', names=['sno', 'sub', 'at','n1','n2','n3'])
print(data)

# making index column
data = pd.read_csv(r'C:\Users\rajku\anagrams.csv',index_col='subidr' )
print(data)


# Importing imp columns only
data = pd.read_csv(r'C:\Users\rajku\anagrams.csv', usecols= ['num1', 'num2'])
print(data)

# Skipping rows perameter
data = pd.read_csv(r'C:\Users\rajku\anagrams.csv', skiprows=[1,2])
print(data)

# importing perticular row (nrow perameter)
data = pd.read_csv(r'C:\Users\rajku\anagrams.csv', nrows=4)
print(data)

# Skip bad rows (some rows can have more values than colums then we can skip them)
# data = pd.read_csv(r'C:\Users\rajku\anagrams.csv', error_bad_lines= False)

def change(name):
    if name =='divided':
        return "HEHEHE"
    else:
        return name
# Converters
data = pd.read_csv(r'C:\Users\rajku\anagrams.csv', converters= {'attnr': change}, nrows=5)
print(data)

# Na values perameter: listing the values as Na/null values 
data = pd.read_csv(r'C:\Users\rajku\anagrams.csv',na_values=['divided'] )
print(data)             

# Loading a Huge dataset in chunks
data = pd.read_csv(r'C:\Users\rajku\anagrams.csv',chunksize=6)          # here chunksize can be a very larger depending upon size of dataset
for chunks in data:
    print(chunks.shape)
