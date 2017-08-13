from rest_framework import serializers

from .models import Tweet


class TweetSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    created_at = serializers.CharField()
    favorite_count = serializers.IntegerField()
    id_str = serializers.CharField()
    source = serializers.CharField()
    text = serializers.CharField()
    user_description = serializers.CharField()
    user_followers_count = serializers.IntegerField()
    user_id_str = serializers.CharField()
    user_location = serializers.CharField()
    user_name = serializers.CharField()
    user_screen_name = serializers.CharField()
    user_verified = serializers.BooleanField()
    
    def create(self, validated_data):
        return Tweet.objects.create(**validated_data)

class TuitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tweet
        fields = ('pk', 'created_at', 'favorite_count', 'id_str', 'source', 'text',
                  'user_description', 'user_followers_count', 'user_id_str', 'user_location',
                  'user_name', 'user_screen_name', 'user_verified')