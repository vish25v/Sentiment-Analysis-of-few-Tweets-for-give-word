import tweepy
from textblob import TextBlob

consumer_key = 'your key here'
consumer_secret = 'your consumer_secret here'

access_token = '800366353295101952-6PrFPKRfTAjiKFOTP1shYd8fNmtsz4l'
access_token_secret = 'czrHj4bSv1U75MG6DfsLvhV5C0WjTGueO0a7jXm35CidI'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('new york')

for tweet in public_tweets:
        print(tweet.text)
        analysis = TextBlob(tweet.text)
        print(analysis.sentiment)
