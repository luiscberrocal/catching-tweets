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