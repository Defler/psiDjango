from rest_framework import serializers
from .models import Comment, Video


# TODO

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'comValue', 'datetime', 'user', 'video'
        ]


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = [
            'title', 'description', 'path', 'datetime', 'user'
        ]
