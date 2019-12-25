import tweepy
import sys
import time


# Set variables and tokens
if sys.argv[1:]:
    consumer_key = sys.argv[1]
    consumer_secret = sys.argv[2]
    access_token = sys.argv[3]
    access_token_secret = sys.argv[4]
else:
    # add the secrets and tokens here
    pass


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)


def rate_limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


# follow-back the followers
for follower in rate_limit_handler(tweepy.Cursor(api.followers).items()):
    print(follower.name)


search_str = 'python'
numOfTweets = 100

for tweet in tweepy.Cursor(api.search, search_str).items(numOfTweets):
    try:
        tweet.favorite()
        print('I liked that tweet!')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
