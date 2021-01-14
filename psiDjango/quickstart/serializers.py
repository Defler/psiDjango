from django.contrib.auth import get_user_model as user_model
from rest_framework import serializers
from .models import Comment, Video

# TODO

User = user_model()


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
        read_only_fields = [
            'id', 'path', 'user'
        ]


class VideoUsersSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = Video
        fields = [
            'user',
            'title'
        ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = [
            'id', 'user'
        ]


class CommentVideosSerializer(serializers.HyperlinkedModelSerializer):
    video = serializers.SlugRelatedField(queryset=Video.objects.all(), slug_field='title')

    class Meta:
        model = Comment
        fields = [
            'video',
            'comValue'
        ]
