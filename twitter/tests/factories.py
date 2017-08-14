
import string

from random import randint
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

    created_at = LazyAttribute(lambda x: faker.date_time_between(start_date="-1y", end_date="now",
                                                           tzinfo=timezone(settings.TIME_ZONE)))
    favorite_count = LazyAttribute(lambda o: randint(1, 100))
    id_str = LazyAttribute(lambda x: FuzzyText(length=15, chars=string.digits).fuzz())
    source = LazyAttribute(lambda x: faker.text(max_nb_chars=150))
    text = LazyAttribute(lambda x: faker.text(max_nb_chars=150))
    user_description = LazyAttribute(lambda x: faker.text(max_nb_chars=300))
    user_followers_count = LazyAttribute(lambda o: randint(1, 100))
    user_id_str = LazyAttribute(lambda x: FuzzyText(length=15, chars=string.digits).fuzz())
    user_location = LazyAttribute(lambda x: faker.text(max_nb_chars=150))
    user_name = LazyAttribute(lambda x: faker.text(max_nb_chars=30))
    user_screen_name = LazyAttribute(lambda x: faker.text(max_nb_chars=60))
    user_verified = Iterator([True, False])

