import csv
import re
import pandas as pd
import numpy as np
from textblob import TextBlob

infile = 'congresstweets.csv'
def clean_tweet(tweet): 
        ''' 
        Utility function to clean tweet text by removing links, special characters 
        using simple regex statements. 
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
 
with open(infile, 'r') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        sentence = row[1]
        clean_tweet(sentence)
        blob = TextBlob(sentence)
        print (sentence)
        print (blob.sentiment.polarity)
        #row[4]= (blob.sentiment.polarity)
        