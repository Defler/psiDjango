from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Comment, Video, VideoCategory

# TODO


class UserVideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Video
        fields = ['url', 'title']


class VideoCategoryVideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Video
        fields = ['url', 'title']


class VideoCategorySerializer(serializers.HyperlinkedModelSerializer):
    videos = VideoCategoryVideoSerializer(many=True, read_only=True)

    class Meta:
        model = VideoCategory
        fields = ['pk', 'url', 'name', 'videos']


class VideoSerializer(serializers.HyperlinkedModelSerializer):
    video_category = serializers.SlugRelatedField(queryset=VideoCategory.objects.all(), slug_field='name')
    comments = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='comment-detail')
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Video
        fields = ['title', 'url', 'video_category', 'description', 'datetime', 'user', 'comments']


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    video = serializers.SlugRelatedField(queryset=Video.objects.all(), slug_field='title')
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ['url', 'comValue', 'datetime', 'user', 'video']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    videos = UserVideoSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['url', 'pk', 'username', 'videos']
