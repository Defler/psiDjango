from django.shortcuts import render
from django.views.generic.base import View, HttpResponse


# Create your views here.

# TODO

class Index(View):
    def get(self, request):
        return HttpResponse('This is index view!')
