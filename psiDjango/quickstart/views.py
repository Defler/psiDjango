from django.shortcuts import render
from django.views.generic.base import View, HttpResponse
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework import generics
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from .serializers import CommentSerializer, VideoSerializer, UserSerializer, VideoCategorySerializer
from .models import Comment, Video, VideoCategory


# Create your views here.

# TODO

class Index(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        return Response({'videos': reverse(VideoList.name, request=request),
                         'comments': reverse(CommentList.name, request=request),
                         'users': reverse(UserList.name, request=request),
                         'video-categories': reverse(VideoCategoryList.name, request=request)
                         })


class VideoCategoryList(generics.ListCreateAPIView):
    queryset = VideoCategory.objects.all()
    serializer_class = VideoCategorySerializer
    name = 'videocategory-list'
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['name']


class VideoCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = VideoCategory.objects.all()
    serializer_class = VideoCategorySerializer
    name = 'videocategory-detail'


class CommentList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-list'
    filter_fields = ['user']
    search_fields = ['comValue']
    ordering_fields = ['datetime']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-detail'
    permission_classes = (IsAuthenticatedOrReadOnly,)


class VideoFilter(FilterSet):
    min_id = NumberFilter(field_name='id', lookup_expr='gte')
    max_id = NumberFilter(field_name='id', lookup_expr='lte')
    title = AllValuesFilter(field_name='title')

    class Meta:
        model = Video
        fields = ['min_id', 'max_id', 'title']


class VideoList(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    name = 'video-list'
    filter_fields = ['title']
    search_fields = ['title']
    ordering_fields = ['datetime']
    permission_classes = (IsAuthenticated,)

    filter_class = VideoFilter

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class VideoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    name = 'video-detail'
    permission_classes = (IsAuthenticatedOrReadOnly,)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'
