from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add/', views.add),
    url(r'^interests/', views.interests),
    url(r'^users/(?P<id>\d+)', views.users),
]
