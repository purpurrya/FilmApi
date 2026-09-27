from django.contrib.auth import get_user_model
from rest_framework import serializers

from project_setup.models import StreamPlatform
from watchlist_app.models import WatchList

User = get_user_model()


class StreamPlatformSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    about = serializers.CharField(max_length=150)
    website = serializers.URLField(max_length=100)


class WatchlistSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=30)
    storyline = serializers.CharField(max_length=200)
    active = serializers.BooleanField()
    # platform = StreamPlatformSerializer()
    # platform = serializers.StringRelatedField()
    # platform = serializers.HyperlinkedRelatedField(view_name='streamplatform-detail-basic-serializer', read_only=True)
    # platform = serializers.HyperlinkedIdentityField(view_name='streamplatform-detail-basic-serializer', read_only=True)
    platform = serializers.SlugRelatedField(
        slug_field="name", queryset=StreamPlatform.objects.all()
    )
    imdb_rating = serializers.FloatField(default=0)
    created = serializers.DateTimeField()
    episodes = serializers.IntegerField(default=0)
    category = serializers.CharField(max_length=30)

    def create(self, validated_data):
        return WatchList.objects.create(**validated_data)


class ReviewSerializer(serializers.Serializer):
    review_user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    rating = serializers.IntegerField()
    description = serializers.CharField(max_length=200)
    watchlist = WatchlistSerializer()
    active = serializers.BooleanField()
    created = serializers.DateTimeField()
    update = serializers.DateTimeField()
