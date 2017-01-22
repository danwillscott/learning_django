from __future__ import print_function
from django.conf.urls import url
from django.shortcuts import render, HttpResponse
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^users$', views.show)
]
