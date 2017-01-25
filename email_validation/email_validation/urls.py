from django.conf.urls import url
from apps.validation import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add),
    url(r'^users$', views.users),
    url(r'^delete/(?P<email_id>\w+)$', views.delete)
]
