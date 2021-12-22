from django.urls import path
from django.contrib import admin
from genwatermark import views

urlpatterns = [
    path('', views.home),
    path('send', views.home),
]