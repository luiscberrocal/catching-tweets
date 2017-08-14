
import string

from random import randint
from unittest.mock import Mock

from pytz import timezone

from django.conf import settings

from factory import Iterator
from factory import LazyAttribute
from factory import SubFactory
from factory import lazy_attribute
from factory.django import DjangoModelFactory, FileField
from factory.fuzzy import FuzzyText, FuzzyInteger
from faker import Factory as FakerFactory

from ..models import Tweet

faker = FakerFactory.create()


class TweetFactory(DjangoModelFactory):
    class Meta:
        model = Tweet
        django_get_or_create = ('id_str',)

    created_at = LazyAttribute(lambda x: faker.date_time_between(start_date="-1y", end_date="now",
                                                           tzinfo=timezone(settings.TIME_ZONE)))
    favorite_count = LazyAttribute(lambda o: randint(1, 100))
    id_str = LazyAttribute(lambda x: FuzzyText(length=100, chars=string.digits).fuzz())
    source = LazyAttribute(lambda x: faker.text(max_nb_chars=150))
    text = LazyAttribute(lambda x: faker.text(max_nb_chars=150))
    user_description = LazyAttribute(lambda x: faker.text(max_nb_chars=300))
    user_followers_count = LazyAttribute(lambda o: randint(1, 100))
    user_id_str = LazyAttribute(lambda x: FuzzyText(length=100, chars=string.digits).fuzz())
    user_location = LazyAttribute(lambda x: faker.text(max_nb_chars=150))
    user_name = LazyAttribute(lambda x: faker.text(max_nb_chars=30))
    user_screen_name = LazyAttribute(lambda x: faker.text(max_nb_chars=60))
    user_verified = Iterator([True, False])


class MockTweetFactory(object):

    def create(self,**kwargs):
        mock_tweet = Mock()
        mock_tweet.created_at = faker.date_time_between(start_date="-1y", end_date="now",
                                                        tzinfo=timezone(settings.TIME_ZONE))
        mock_tweet.favorite_count = 2
        mock_tweet.id_str = FuzzyText(length=100, chars=string.digits).fuzz()
        mock_tweet.source = faker.text(max_nb_chars=150)
        mock_tweet.text = faker.text(max_nb_chars=150)
        mock_tweet.user = Mock()
        mock_tweet.user.description = faker.text(max_nb_chars=300)
        mock_tweet.user.followers_count = 2
        mock_tweet.user.id_str = FuzzyText(length=100, chars=string.digits).fuzz()
        mock_tweet.user.location = faker.country()
        mock_tweet.user.name = faker.user_name()
        mock_tweet.user.screen_name = faker.name()
        mock_tweet.user.verified = False
        return mock_tweet