from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

# TODO

class Video(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField(max_length=300)
    path = models.CharField(max_length=45)
    datetime = models.DateTimeField(blank=False, null=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)


class Comment(models.Model):
    comValue = models.TextField(max_length=300)
    datetime = models.DateTimeField(blank=False, null=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
