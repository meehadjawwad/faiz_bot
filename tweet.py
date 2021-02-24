# coding=utf-8

# importing the libraries
# the keys_for_faiz_bot and lyrics libraries are .py files

import keys_for_faiz_bot
import lyrics
import tweepy
import time
from random import *

# setting up the authentication framework

consumer_key = keys_for_faiz_bot.consumer_key
consumer_secret = keys_for_faiz_bot.consumer_secret

key = keys_for_faiz_bot.key
secret = keys_for_faiz_bot.secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

# defining variables to be used afterwards

FILE_NAME = 'last_seen.txt'

lyrics = lyrics.lyrics

# defining a function to read the most recent tweet_id

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

# defining a function to write the most recent tweet_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

# defining the main reply function

def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode = 'extended')
    for tweet in reversed(tweets):
        print(str(tweet.id), '-', tweet.full_text)
        random_number = randint(0, len(lyrics))
        lyric = lyrics[random_number]
        lyric = str(lyric)
        api.update_status("@" + tweet.user.screen_name + lyrics[randint(0, len(lyrics))], tweet.id)
        store_last_seen(FILE_NAME, tweet.id)

# defining the main tweet function

def send_tweet():
    api.update_status(" " + lyrics[randint(0, len(lyrics))])

# defining the main function by combining the two main functions

while True:
    send_tweet()
    for i in range(0, 960):
        reply()
        time.sleep(15)