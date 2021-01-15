from django.contrib.auth.models import User

#from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework import serializers

from . import views
from .models import VideoCategory, Comment, Video
from .serializers import CommentSerializer
#import json


# Create your tests here.

# TODO

class VideoCategoryTests(APITestCase):
    def post_video_category(self, name):
        url = reverse(views.VideoCategoryList.name)
        data = {
            'name': name
        }
        response = self.client.post(url, data, format='json')
        return response

    def test_post_and_get_category(self):
        new_name = 'NewCategory'
        response = self.post_video_category(new_name)
        # print(response.status_code)
        # print(response)
        assert response.status_code == status.HTTP_201_CREATED
        assert VideoCategory.objects.count() == 1
        assert VideoCategory.objects.get().name == new_name



# class CommentTest(APITestCase):
#     def setUp(self):
#         # Create some users
#         self.user_1 = User.objects.create_user(username='admin', password='pwdpwd', email='admin@mail.com')
#         self.vidcat_1 = VideoCategory.objects.create(name="TestCat")
#         self.video_1 = Video.objects.create(video_category=self.vidcat_1, title='test', description='desc', datetime='2021-02-05T00:06:00Z', user=self.user_1)
#
#     def post_comment(self, comValue, dateTime):
#         video = self.video_1
#         video = CommentSerializer(instance=video)
#         print(video)
#         url = reverse(views.CommentList.name)
#         data = list({
#             'comValue': comValue,
#             'datetime': dateTime,
#             'video': video
#         })
#         response = self.client.post(url, json.dumps(data), format='json')
#         return response
#
#     def test_post_and_get_comment(self):
#         self.client.login(username='admin', password='pwdpwd')
#         new_comValue = 'NewComValue'
#         new_dateTime = '2021-02-05T00:06:00Z'
#         response = self.post_comment(new_comValue, new_dateTime)
#         print(response.status_code)
#         print(response)
#         print(response.json())
#         assert response.status_code == status.HTTP_201_CREATED
#         assert VideoCategory.objects.count() == 1
#         assert VideoCategory.objects.get().name == new_comValue
