import tweepy

from django.conf import settings
from django.core.management import BaseCommand

auth = tweepy.OAuthHandler(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET)

auth.set_access_token(settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_TOKEN_SECRET)

api = tweepy.API(auth)


class Command(BaseCommand):

    help = 'Setup a simple tweet feed'

    def handle(self, **options):
        user = api.get_user('luiscberrocal')
        print(user.screen_name)
        print(user.followers_count)
        count = 1
        for friend in user.friends():
            print('{}. {}'.format(count, friend.screen_name))
            count += 1

