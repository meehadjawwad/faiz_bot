# coding=utf-8

import keys_for_faiz_bot
import lyrics
import tweepy
import time
from random import *

consumer_key = keys_for_faiz_bot.consumer_key
consumer_secret = keys_for_faiz_bot.consumer_secret

key = keys_for_faiz_bot.key
secret = keys_for_faiz_bot.secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

FILE_NAME = 'last_seen.txt'

lyrics = lyrics.lyrics


def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id


def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return


def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode = 'extended')
    for tweet in reversed(tweets):
        print(str(tweet.id), '-', tweet.full_text)
        random_number = randint(0, len(lyrics))
        lyric = lyrics[random_number]
        lyric = str(lyric)
        api.update_status("@" + tweet.user.screen_name + lyrics[randint(0, len(lyrics))], tweet.id)
        store_last_seen(FILE_NAME, tweet.id)


def send_tweet():
    api.update_status(" " + lyrics[randint(0, len(lyrics))])


while True:
    send_tweet()
    for i in range(0, 960):
        reply()
        time.sleep(15)