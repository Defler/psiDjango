from django.shortcuts import render
from django.views.generic.base import View, HttpResponse

# Create your views here.

# TODO

class Index(View):
    template_name = 'index.html'
    def get(self, request):
        variableA = 'dymy here'
        return render(request, self.template_name, {'variable': variableA})


class NewVideo(View):
    template_name = 'new_video.html'
    def get(self, request):
        variableA = 'New Video'
        return render(request, self.template_name, {'variable': variableA})



