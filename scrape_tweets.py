# Adam Munawar Rahman, March 2020
# Code to scrape Tweets from a specific account
# and append them to a .csv

import tweepy
import csv
 
access_key = <access_key>
access_secret = <access_secret>

consumer_key = <consumer_key>
consumer_secret = "<consumer_secret"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
 
api = tweepy.API(auth)

tweets = api.user_timeline(screen_name="@FDNY")

# Pull in notable data for each Tweet and prepare them for CSV writing

list_for_csv = []

for tweet in tweets:
    string_to_join = []
    string_to_join.append(tweet.text)
    string_to_join.append(tweet.created_at)
    string_to_join.append(retweeted_status)
    string_to_join.append(retweet_count)
    string_to_join.append(favorite_count)
    
    tweet_entry = '-'.join(string_to_join)
    list_for_csv.append(tweet_entry)


with open('csv-data/raw_tweets.csv', 'w+', newline ='') as f: 
    write = csv.writer(f)
    write.writerows(list_for_csv)