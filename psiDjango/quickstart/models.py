from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

# TODO

class VideoCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Video(models.Model):
    video_category = models.ForeignKey(VideoCategory, related_name='videos', on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    description = models.TextField(max_length=300)
    datetime = models.DateTimeField(blank=False, null=False)
    user = models.ForeignKey('auth.User', related_name='videos', on_delete=models.CASCADE)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    comValue = models.TextField(max_length=300)
    datetime = models.DateTimeField(blank=False, null=False)
    user = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    video = models.ForeignKey(Video, related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ('comValue',)

    def __str__(self):
        return self.comValue

