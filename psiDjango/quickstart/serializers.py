from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Comment, Video

# TODO


class VideoSerializer(serializers.HyperlinkedModelSerializer):
    comments = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='comment-detail')
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Video
        fields = ['url', 'title', 'description', 'datetime', 'user', 'comments']


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    video = serializers.SlugRelatedField(queryset=Video.objects.all(), slug_field='title')
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ['url', 'comValue', 'datetime', 'user', 'video']


class UserCommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['url', 'comValue']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    comments = UserCommentSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['url', 'pk', 'username', 'comments']
