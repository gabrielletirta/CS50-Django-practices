# This line imports the 'path' function from Django 'urls' module. 'path' function is used to define URL patterns.
from django.urls import path 

#this line imports the 'views' module from the current directory . The (.) represents the current directory
from . import views

# urlpatterns is a configuration variables in Django used to define url attern and the associated view function or class that should handle requests matching the pattern.
urlpatterns = [
    path("", views.index, name="index")
]