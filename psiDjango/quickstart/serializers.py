from rest_framework import serializers
from .models import Comment, Video


# TODO

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = [
            'id'
        ]


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
        read_only_fields = [
            'id', 'path'
        ]