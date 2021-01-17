from django.contrib.auth.models import User
#from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework import serializers
from django import urls
from django.utils.http import urlencode
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

    def test_update_video_category(self):
        video_category_name = 'porn'
        response = self.post_video_category(video_category_name)
        url = urls.reverse(views.VideoCategoryDetail.name, None, {response.data['pk']})
        updated_video_category_name = 'New porn'
        data = {'name': updated_video_category_name}
        patch_response = self.client.patch(url, data, format='json')
        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['name'] == updated_video_category_name

    def test_get_video_category(self):
        video_category_name = 'porn'
        response = self.post_video_category(video_category_name)
        url = urls.reverse(views.VideoCategoryDetail.name, None, {response.data['pk']})
        get_response = self.client.patch(url, format='json')
        assert get_response.status_code == status.HTTP_200_OK
        assert get_response.data['name'] == video_category_name

    def test_filter_video_category_by_name(self):
        video_category_name_one = 'horror'
        video_category_name_two = 'porn'
        self.post_video_category(video_category_name_one)
        self.post_video_category(video_category_name_two)
        filter_by_name = {'name': video_category_name_one}
        url = '{0}?{1}'.format(reverse(views.VideoCategoryList.name), urlencode(filter_by_name))
        print(url)
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['name'] == video_category_name_one


