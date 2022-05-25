import time

import tweepy

auth = tweepy.OAuth2BearerHandler("AAAAAAAAAAAAAAAAAAAAAEVkbgEAAAAA8LPNuhjuuULdD2S17N5Ik%2BO3iOM%3DYQ9dDc2VJTVJFhn20oxxvmXHpITvmJ7uvfCRQ0VAQtrkdxsfO0")
api = tweepy.API(auth)

s = input("")

def get_related_tweets(text_query):
    # list to store tweets
    tweets_list = []
    # no of tweets
    count = 50
    try:
        # Pulling individual tweets from query
        for tweet in api.search_tweets(q=text_query, count=count):
            print(tweet.text)
            print()
    except BaseException as e:
        print('failed on_status,', str(e))
        time.sleep(3)

    print(tweets_list)

get_related_tweets("trump")