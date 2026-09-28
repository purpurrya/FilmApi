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

    def validate_title(self, value):
        if "@" in value:
            serializers.ValidationError("Invalid Title")
        return value

    def validate_storyline(self, value):
        if "@" in value:
            serializers.ValidationError("Invalid Storyline")
        return value

    def validate_category(self, value):
        if value not in ["MOVIE", "SERIES"]:
            serializers.ValidationError("Not a valid category")
        return value

    def validate(self, data):
        title = data.get("title", None)
        storyline = data.get("storyline", None)
        if (title and storyline) and (len(title) > len(storyline)):
            raise serializers.ValidationError(
                "Length of thetitle is bigger than storyline"
            )
        return super().validate(data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.storyline = validated_data.get("storyline", instance.storyline)
        instance.active = instance.title = validated_data.get("active", instance.active)
        instance.platform = validated_data.get("platform", instance.platform)
        instance.imdb_rating = validated_data.get("imdb_rating", instance.imdb_rating)
        instance.created = validated_data.get("created", instance.created)
        instance.episodes = validated_data.get("episodes", instance.episodes)
        instance.category = validated_data.get("category", instance.category)
        instance.title = validated_data.get("storyline", instance.storyline)
        instance.save()
        return instance


class ReviewSerializer(serializers.Serializer):
    review_user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    rating = serializers.IntegerField()
    description = serializers.CharField(max_length=200)
    watchlist = WatchlistSerializer()
    active = serializers.BooleanField()
    created = serializers.DateTimeField()
    update = serializers.DateTimeField()
