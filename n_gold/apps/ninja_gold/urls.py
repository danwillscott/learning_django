#  TODO Fix this to apps views
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^gold$', views.gold),
]
