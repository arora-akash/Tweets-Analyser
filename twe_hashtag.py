import tweepy
import csv
import pandas as pd
import json

access_token = "2901722802-aZuvqYCV4wLbl6G5ZX5rbfKh54XwBK6HjJSnZYM"
access_token_secret = "21p1V3tNX698QKKug0Z4v9kUQ4bp3vkMb32143dvgDzWo"
consumer_key = "n30IbetTPayHbruKWryrd39v3"
consumer_secret = "ERJo6ZHexudlL23eoebJRSsey9cbAzptPOngcZT8kqFgJj6DCK"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('bjptweets.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)
f = open('FILENAME.json', 'a')

for tweet in tweepy.Cursor(api.search,q='#BJP OR #bjp OR BJP OR Modi OR modi OR abkibaarmodisarkar',geocode="21.146633,79.088860,1756km",count=100,
                           lang="en").items():
    print (tweet.created_at, tweet.text, tweet.user.location, tweet.user.followers_count)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'),tweet.user.location.encode('utf-8'), tweet.user.followers_count])
