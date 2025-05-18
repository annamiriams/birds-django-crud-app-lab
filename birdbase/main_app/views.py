from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    # The HttpResponse object we used is the simplest way to return content in Django. As we progress, we will explore more sophisticated methods such as rendering templates which allow for more dynamic and interactive web pages.
    return HttpResponse('<h1>BirdBase</h1>')

def about(request):
    return HttpResponse('<h1>About</h1>')