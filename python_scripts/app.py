import tweepy

# Twitter API credentials
consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_token = "your_access_token"
access_token_secret = "your_access_token_secret"

# The topic or trend to search for
search_topic = "your_search_topic"

# Create an OAuthHandler instance
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create an API object
api = tweepy.API(auth)

# Search and retweet tweets with the specified topic
tweets = tweepy.Cursor(api.search, q=search_topic).items()

for tweet in tweets:
    try:
        # Retweet the tweet
        api.retweet(tweet.id)
        print("Retweeted a tweet!")
    except tweepy.TweepError as e:
        print(e.reason)

print("Retweet process completed.")
