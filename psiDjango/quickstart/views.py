from django.shortcuts import render
from django.views.generic.base import View, HttpResponse
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework import generics

from .serializers import CommentSerializer, VideoSerializer, VideoUsersSerializer, CommentVideosSerializer
from .models import Comment, Video


# Create your views here.

# TODO


class Index(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        data = {
            'test Index'
            'data'
        }
        return Response(data)


class CommentApiView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        queryset = Comment.objects.all()
        # comment = queryset.first()
        # serializer = CommentSerializer(comment)
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class CommentListApiView(generics.ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filterset_fields = ['user']
    search_fields = ['video']
    ordering_fields = ['datetime']


class CommentUpdateApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class VideoApiView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        queryset = Video.objects.all()
        # comment = queryset.first()
        # serializer = CommentSerializer(comment)
        serializer = VideoSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class VideoFilter(FilterSet):
    min_id = NumberFilter(field_name='id', lookup_expr='gte')
    max_id = NumberFilter(field_name='id', lookup_expr='lte')
    title = AllValuesFilter(field_name='title')

    class Meta:
        model = Video
        fields = ['min_id', 'max_id', 'title']


class VideoListApiView(generics.ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_class = VideoFilter
    name = 'VideosList'





class VideoUpdateApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class VideoUsersView(generics.ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Video.objects.all()
    serializer_class = VideoUsersSerializer


class CommentVideosView(generics.ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Comment.objects.all()
    serializer_class = CommentVideosSerializer
