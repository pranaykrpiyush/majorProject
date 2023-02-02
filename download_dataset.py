import tweepy
import csv

# Add your Twitter API credentials
consumer_key = "eGFRLcG4b6a91TE7DtG5zwrjT"
consumer_secret = "a6MVrWlyqLtDYDun0yPraLG35iWDItzXcdRtkGv0602pPT7W2G"
access_token = "1109516604575043584-POPzgSoVocK6b1ekvtI70GJRqo38IL"
access_token_secret = "6eOXdRBrffjgNmyvQRSuyTfJms9dnii2rI2YXFU2fCUbG"

# Authenticate the API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Define a list to store the tweets
tweets = api.user_timeline(screen_name='pranaykrpiyush', count=200)

# Step 3: Extract the tweets, timestamps, and sources
tweet_text = [tweet.text for tweet in tweets]
timestamps = [tweet.created_at for tweet in tweets]
sources = [tweet.source for tweet in tweets]

# Step 4: Write the tweets, timestamps, and sources to a .tsv file
with open('tweets.tsv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f, delimiter='\t')
    for i in range(len(tweets)):
        writer.writerow([tweet_text[i], timestamps[i], sources[i]])
