import tweepy
from django.conf import settings
from django.core.management import BaseCommand


class TweepyCommand(BaseCommand):

    def __init__(self, stdout=None, stderr=None, no_color=False):
        auth = tweepy.OAuthHandler(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET)

        auth.set_access_token(settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_TOKEN_SECRET)

        self.api = tweepy.API(auth)
        super(TweepyCommand, self).__init__(stdout, stderr, no_color)


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        if status_code == 420:
            return False

class TweetAdapter(object):

    def convert(self, tweet):
        tweet_data = dict()
        tweet_data['created_at'] = tweet.created_at
        tweet_data['favorite_count'] = tweet.favorite_count
        tweet_data['id_str'] = tweet.id_str
        tweet_data['source'] = tweet.source
        tweet_data['text'] = tweet.text
        tweet_data['user_description'] = tweet.user.description
        tweet_data['user_followers_count'] = tweet.user.follower_count
        tweet_data['user_id_str'] = tweet.user.id_str
        tweet_data['user_location'] = tweet.user.location
        tweet_data['user_name'] = tweet.user.name
        tweet_data['user_screen_name'] = tweet.user.screen_name
        tweet_data['user_verified'] = tweet.user.verified
        return tweet_data

