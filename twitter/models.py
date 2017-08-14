from django.db import models

# Create your models here.

class Tweet(models.Model):
    created_at = models.DateTimeField()
    favorite_count = models.IntegerField(default=0)
    id_str = models.CharField(max_length=100)
    source = models.CharField(max_length=150)
    text = models.CharField(max_length=150)
    user_description = models.CharField(max_length=300)
    user_followers_count = models.IntegerField(default=0)
    user_id_str = models.CharField(max_length=100)
    user_location = models.CharField(max_length=150)
    user_name = models.CharField(max_length=30)
    user_screen_name = models.CharField(max_length=60)
    user_verified = models.BooleanField(default=False)