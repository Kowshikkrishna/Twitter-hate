import time
import pandas as pd
pd.set_option('display.max_colwidth', 1000)
import tweepy

auth = tweepy.OAuth2BearerHandler("AAAAAAAAAAAAAAAAAAAAAEVkbgEAAAAA8LPNuhjuuULdD2S17N5Ik%2BO3iOM%3DYQ9dDc2VJTVJFhn20oxxvmXHpITvmJ7uvfCRQ0VAQtrkdxsfO0")
api = tweepy.API(auth)

def get_related_tweets(text_query):
    # list to store tweets
    tweets_list = []
    # no of tweets
    count = 100
    try:
        # Pulling individual tweets from query
        for tweet in api.search_tweets(q=text_query, count=count):
            #print(tweet.text)
            # Adding to list that contains all tweets
            tweets_list.append({'created_at': tweet.created_at,
                                'tweet_id': tweet.id,
                                'tweet_text': tweet.text})
        return pd.DataFrame.from_dict(tweets_list)

    except BaseException as e:
        print('failed on_status,', str(e))
        time.sleep(3)