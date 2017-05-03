import tweepy
import json


def load_credentials():
    # loads all authorization info required for access Twitter api
    with open('credentials.json') as f:
        cred_info = json.loads(f.read())
    return cred_info['consumer_key'], cred_info['consumer_secret'], \
           cred_info['access_token'], cred_info['access_token_secret']


def setup_twitter_api():
    # setups api using credentials provided in config file
    consumer_key, consumer_secret, access_token, access_token_secret = load_credentials()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api


def get_tweets_for_query(query, tweets_lang='en', cnt=15):
    # returns list of tweets text for provided query
    api = setup_twitter_api()
    search_results = api.search(query, lang=tweets_lang, count=cnt)
    return [tweet.text for tweet in search_results]
