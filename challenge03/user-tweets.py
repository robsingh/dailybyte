import csv
import os
import tweepy
from collections import namedtuple
from config import BEARER_TOKEN  # You will need to use a bearer token for v2 API

DEST_DIR = 'data'
EXT = 'csv'
NUM_TWEETS = 100

Tweet = namedtuple('Tweet', ['id', 'created_at', 'text'])

class UserTweets(object):

    def __init__(self, handle, max_id=None):
        """Use tweepy.Client with bearer token to create API interface for Twitter v2."""
        self.handle = handle
        self.max_id = max_id
        self.client = tweepy.Client(bearer_token=BEARER_TOKEN)
        self.user_id = self._get_user_id()
        self._tweets = list(self._get_tweets())
        self._save_tweets()

    def _get_user_id(self):
        """Get the user ID for the handle."""
        user = self.client.get_user(username=self.handle)
        return user.data.id

    def _get_tweets(self):
        """Fetch tweets from the user timeline using Twitter API v2."""
        tweets = self.client.get_users_tweets(
            id=self.user_id, 
            max_results=NUM_TWEETS, 
            tweet_fields=['created_at']
        )
        return (Tweet(tweet.id, tweet.created_at, tweet.text) for tweet in tweets.data)

    def _save_tweets(self):
        """Use the csv module (csv.writer) to write out the tweets."""
        if not os.path.exists(DEST_DIR):
            os.makedirs(DEST_DIR)

        file_path = os.path.join(DEST_DIR, f"{self.handle}.{EXT}")

        with open(file_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(Tweet._fields)  # Write the header
            writer.writerows(self._tweets)  # Write the tweet data

    def __len__(self):
        """Returns the number of tweets fetched."""
        return len(self._tweets)

    def __getitem__(self, pos):
        """Return a tweet at a specific position."""
        return self._tweets[pos]


if __name__ == "__main__":
    for handle in ('pybites', '_juliansequeira', 'bbelderbos'):
        print('--- {} ---'.format(handle))
        user = UserTweets(handle)
        for tw in user[:5]:
            print(tw)
        print()
