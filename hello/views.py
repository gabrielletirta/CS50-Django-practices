from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#This is the functions that will be used on urls.py
def index(request):
    return render(request, "hello/index.html") #this is how we return from html files, not just strings

def gaby(request):
    return HttpResponse("Hello, Gaby")

def meepy(request):
    return HttpResponse("Hello Meepy!")

#This is when we want to use arbitary names, so we dont need to define each one of them. and w
def greet(request, name):
    return render(request, "hello/greet.html",{
        "name": name.capitalize()
    }) ##this is how we do if we want to 'customize' names through our HTML files
