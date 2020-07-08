import tweepy
import time
from random import *

consumer_key = 'YjKgsOENgv5w86q8PQXFIO53R'
consumer_secret = 'FzqMGWoCRdcdwXBZsyPpLla19ksdkoBjsQExjRgxKPELoqsbUm'

key = '1278128329611259909-tmundA5aPA8LQRZdHsJuPFhDRJNjF7'
secret = 'PMawXveiCFbijLm1C6HZIOl5Es8ZcymMRJQwJIM1RIyyc'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

search = '#FaizAhmadFaiz'
nrTweets = 500

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
        try:
            tweet.favorite()
            print("Tweet Liked")
            time.sleep(8)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break