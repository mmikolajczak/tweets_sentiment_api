import tweepy
import json


def load_credentials():
    # loads all authorization info required for access Twitter api
    with open('credentials.json') as f:
        cred_info = json.loads(f.read())
    return cred_info['consumer_key'], cred_info['consumer_secret'], \
           cred_info['access_token'], cred_info['access_token_secret']


def setup_twitter_api():
    consumer_key, consumer_secret, access_token, access_token_secret = load_credentials()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api


def main():
    api = setup_twitter_api()
    search_results = api.search('Trump', lang='en')

    # quick look up of results
    for tweet in search_results:
        print(tweet.text)
        print('\n\n')

    print('Total:', len(search_results))

if __name__ == '__main__':
    main()
