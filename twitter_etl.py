import tweepy
import pandas as pd
import json
from datetime import datetime

access_key = 'yK3kS1ByFkUSNehlDgCkTCLiQ'
access_secret='Njg54afpfZA1KrZjWLYwF82yjCmncwa6FSWslzIP7qAsZpp6TD'
consumer_key='1689088493715427328-J7ovJvokPaBJRAr1M0YgRo83JmrqK1'
consumer_secret='Vdg7Iwsec7TjsRtGgnmiUVZnqVzVW4BkCz48QCJArL19B'

# Twitter authentication
auth = tweepy.OAuthHandler(access_key, access_secret)   
auth.set_access_token(consumer_key, consumer_secret) 

# # # Creating an API object 
api = tweepy.API(auth)
tweets = api.user_timeline(screen_name='@elonmusk',count=200,include_rts = False,tweet_mode = 'extended')
print(tweets)


list = []
for tweet in tweets:
        text = tweet._json["full_text"]

        refined_tweet = {"user": tweet.user.screen_name,
                        'text' : text,
                        'favorite_count' : tweet.favorite_count,
                        'retweet_count' : tweet.retweet_count,
                        'created_at' : tweet.created_at}
        
        list.append(refined_tweet)

df = pd.DataFrame(list)
df.to_csv('refined_tweets.csv')
