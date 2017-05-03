import textblob


def get_sentiment_score(tweets):
    # returns average sentiment score from tweets, during calculation ignores the ones with 0
    # polarity (as they have in most cases just informational value, not contain opinion)
    sentiment_pts = 0
    non_informational_cnt = 0

    for tweet in tweets:
        tb = textblob.TextBlob(tweet)
        if tb.sentiment.polarity != 0:
            sentiment_pts += float(tb.sentiment.polarity)
            non_informational_cnt += 1

    score = sentiment_pts / non_informational_cnt if non_informational_cnt != 0 else 0
    return score, non_informational_cnt
