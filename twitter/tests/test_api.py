from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient


class TestTweetViewSet(TestCase):

    def test_(self):
        url = reverse('twitter/')
        client = APIClient()
        response = client.get(url)
        self.assertEqual('', response.data)

