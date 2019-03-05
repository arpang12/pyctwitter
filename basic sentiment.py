import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key = 'Z9FlurhrJy6Jm5AL0JimtKfQz'
consumer_secret = 'xGKs0c8Je7rnh2vclVGAGryborwLsoAYLgMwVYU37O3mmx8CMx'

access_token = '974683305923653632-t7xMXezC21kq6Q2mpQ1Wwl4xFrqwzEc'
access_token_secret = 'k9PxQV4O0QGsrpxO9v4GaqFIidazqTwwgxltsINAyxaB3'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Step 3 - Retrieve Tweets
public_tweets = api.search(input('Enter the tweet you wanna search'))

# CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
# and label each one as either 'positive' or 'negative', depending on the sentiment
# You can decide the sentiment polarity threshold yourself


for tweet in public_tweets:
    print(tweet.text)

    # Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    csvFile = open('chay.csv','a')
    csvWriter =csv.writer(csvFile)