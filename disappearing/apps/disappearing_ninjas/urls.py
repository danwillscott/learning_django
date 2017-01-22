from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
        url(r'^$', views.no_ninjas),
        url(r'^ninjas/$', views.index),
        url(r'^ninjas/(?P<ninja_id>\w+)$', views.ninjas)
]
