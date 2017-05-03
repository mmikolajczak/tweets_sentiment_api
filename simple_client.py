import requests
import argparse
import json


def get_human_like_interpretation(score):
    # translates score value to more human readable form
    score = float(score)
    if -1 <= score <= -0.76:
        return 'terrifyingly negative'
    elif -0.75 <= score <= -0.51:
        return 'really negative'
    elif -0.5 <= score <= -0.26:
        return 'negative'
    elif -0.25 <= score <= -0.06:
        return 'quite negative'
    elif -0.05 <= score <= 0.05:
        return 'neutral'
    elif 0.06 <= score <= 0.25:
        return 'quite positive'
    elif 0.026 <= score <= 0.5:
        return 'positive'
    elif 0.51 <= score <= 0.75:
        return 'really positive'
    if 0.76 <= score <= 1:
        return 'incredibly positive'


def print_summary(server_response):
    # just printing summary of received json data in more readable form
    try:
        data = json.loads(server_response)
        print('Query:\t', data['query'])
        print('Meaningful tweets analysed:\t', data['sample_size'])
        print('Tweets semantic polarity score:\t', data['score'])
        print('More "human-like" interpretation:\t', 'Tweets about this topic are ' +
              get_human_like_interpretation(data['score']))
    except Exception:
        raise Exception('error during processing server response')


def get_cmd_args():
    # parses command line arguments
    ap = argparse.ArgumentParser()
    ap.add_argument('-q', '--query', required=True, help='Phrase that tweets be matched against')
    ap.add_argument('-l', '--language', help='Language of tweets')
    return vars(ap.parse_args())


def main():
    # client workflow
    try:
        args = get_cmd_args()
        params = {'query': args['query']}
        if 'language' in args:
            params['lang'] = args['language']

        try:
            r = requests.get('http://localhost:5000/sentiment_api/v1.0/sentiment_score', json=params)
            r.raise_for_status()
        except Exception:
            raise Exception('error with server connection/request parameters')

        print_summary(r.text)
    except Exception as e:
        print('Unfortunately, an error occurred:', e)

if __name__ == '__main__':
    main()
