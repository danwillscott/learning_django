
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register', views.register),
    url(r'^log_in', views.user_login),
    url(r'^log_out', views.user_logout),
    url(r'^edit/(?P<user_name>\w+)', views.edit),
]
