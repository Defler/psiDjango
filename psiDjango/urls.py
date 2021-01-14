"""psiDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from psiDjango.quickstart import views
from psiDjango.quickstart import views
from psiDjango.quickstart.views import Index, CommentApiView, CommentVideosView, CommentListApiView, CommentUpdateApiView, VideoApiView, VideoUsersView, VideoListApiView, VideoUpdateApiView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='IndexApiView'),
    path('comments', CommentApiView.as_view(), name='CommentApiView'),
    path('commentsVideos', CommentVideosView.as_view(), name='CommentVideosApiView'),
    path('commentsList', CommentListApiView.as_view(), name='CommentListApiView'),
    path('comments/<int:pk>', CommentUpdateApiView.as_view(), name='CommentUpdateApiView'),
    path('videos', VideoApiView.as_view(), name='VideoApiView'),
    path('videosUsers', VideoUsersView.as_view(), name='VideoUsersApiView'),
    path('videosList', VideoListApiView.as_view(), name='VideoListApiView'),
    path('videos/<int:pk>', VideoUpdateApiView.as_view(), name='VideoUpdateApiView'),
]
