from textblob import TextBlob
import tweepy

consumer_Key = 'Z9FlurhrJy6Jm5AL0JimtKfQz'
consumer_Secret = 'xGKs0c8Je7rnh2vclVGAGryborwLsoAYLgMwVYU37O3mmx8CMx'
access_Token = '974683305923653632-t7xMXezC21kq6Q2mpQ1Wwl4xFrqwzEc'
access_Token_Secret = 'k9PxQV4O0QGsrpxO9v4GaqFIidazqTwwgxltsINAyxaB3'
auth = tweepy.OAuthHandler(consumer_Key, consumer_Secret)
auth.set_access_token(access_Token, access_Token_Secret)
api = tweepy.API(auth)


searchTerm = input("Enter Keyword/Tag to search about: ")
NoOfTerms = int(input("Enter how many tweets to search: "))

for tweet in public_tweet:
    analysis =TextBlob(tweet.text)
    print(analysis)