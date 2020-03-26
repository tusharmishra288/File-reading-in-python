
import pandas as pd
import re
# url to retrieve
url = 'https://en.wikipedia.org/wiki/List_of_airports_by_IATA_code:_A'

# extract the data from the HTML
#we use [0] since there are two tables on the html page we want to extract the first table
data=pd.read_html(url)
url_read = pd.read_html(url, header = 0)[0]

# regular expression to find any white spaces in a string
s=url_read.columns
s=list(s)
for p in range(len(s)):
    if "\xa0" in s[p]:
        s[p]=s[p].replace("\xa0","_")
url_read.columns=s

space = re.compile(r'\s+')

def fix_string_spaces(columnsToFix):
    
       # Converts the spaces in the column name to underscore
    
    tempColumnNames = [] # list to hold fixed column names

    # loop through all the columns
    for item in columnsToFix:
        # if space is found
        if space.search(item): #scans string followed by whitespace
            #split the strings around whitespaces and join them back using underscore
            # fix and append to the list
            tempColumnNames.append('_'.join(space.split(item)))
        else:
            # else append the original column name
            tempColumnNames.append(item)

    return tempColumnNames

url_read.columns = fix_string_spaces(url_read.columns)
url_read.dropna(thresh=6,inplace=True)
url_read.index = range(0,len(url_read))
print(url_read.head(10)[['IATA', 'Airport_name']])
print(url_read[20:30][['IATA', 'Airport_name']])