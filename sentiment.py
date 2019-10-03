import csv
import re
import pandas as pd
import numpy as np
from textblob import TextBlob
from googletrans import Translator

infile = 'congresstweets.csv'
def clean_tweet(tweet): 
        ''' 
        Utility function to clean tweet text by removing links, special characters 
        using simple regex statements. 
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
with open('outco.csv','w') as writeFile:
	with open(infile, 'r') as csvfile:
	    rows = csv.reader(csvfile)
	    writer = csv.writer(writeFile)
	    writer.writerow(['Date', 'Tweets', 'Location', 'Sentiment Polarity'])
	    for row in rows:
		sentence = row[1]
		sentence = clean_tweet(sentence)
		a = Translator().translate(sentence)
		sentence = a.text
		date = str(row[0])
		twe = str(row[1])
		loc = str(row[2])
		
		blob = TextBlob(sentence)
		print (sentence)
		print (blob.sentiment.polarity)
		pol = float(blob.sentiment.polarity)		
		writer.writerow([date, twe, loc, pol])
		#row[4]= (blob.sentiment.polarity)
