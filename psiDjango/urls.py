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
from psiDjango.quickstart.views import Index, NewVideo, CommentApiView, IndexApiView, VideoApiView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('home', Index.as_view()),  # path('index', views.Index.as_view())
    path('new_video', NewVideo.as_view()),
    path('commentsApi', CommentApiView.as_view(), name='testCommentApiView'),
    path('', IndexApiView.as_view(), name='testIndexApiView'),
    path('videosApi', VideoApiView.as_view(), name='testVideoApiView'),
]
