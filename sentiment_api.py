from get_searched_tweets import get_tweets_for_query
from sentiment_analysis import get_sentiment_score
from flask import Flask, jsonify, request, abort

app = Flask(__name__, static_url_path="")


@app.route('/sentiment_api/v1.0/sentiment_score', methods=['GET'])
def get_sentiment_score():
    if not request.json or 'query' not in request.json:
        abort(400)
    query = request.json['query']
    lang = request.json.get('lang', 'en')
    sample_size = 50 # for now not available to be specified by request

    tweets = get_tweets_for_query(query, lang, sample_size)
    sentiment_score, used_tweets = get_sentiment_score(tweets)

    return jsonify({'query': query, 'score': sentiment_score, 'verbal_score': 'TBD', 'sample_size': used_tweets})

if __name__ == '__main__':
    app.run(debug=True)
