from django.urls import path
from . import views

#We took funcitons from urls.py and use them to below urlpatterns
urlpatterns = [
    path("", views.index, name="index"),
    path("gaby", views.gaby, name="gaby"),
    path("meepy", views.meepy, name="meepy"),
    path("<str:name>", views.greet, name="greet")
]