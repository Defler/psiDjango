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
from psiDjango.quickstart.views import Index, CommentList, CommentDetail, \
    VideoList, VideoDetail, VideoCategoryList, VideoCategoryDetail, UserList, UserDetail

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='IndexApiView'),

    path('comments', CommentList.as_view(), name=views.CommentList.name),
    path('comments/<int:pk>', CommentDetail.as_view(), name=views.CommentDetail.name),

    path('videos', VideoList.as_view(), name=views.VideoList.name),
    path('videos/<int:pk>', VideoDetail.as_view(), name=views.VideoDetail.name),

    path('users', UserList.as_view(), name=views.UserList.name),
    path('users/<int:pk>', UserDetail.as_view(), name=views.UserDetail.name),

    path('video-categories', VideoCategoryList.as_view(), name=views.VideoCategoryList.name),
    path('video-categories/<int:pk>', VideoCategoryDetail.as_view(), name=views.VideoCategoryDetail.name)
]
