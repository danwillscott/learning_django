from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index_alt),
    url(r'^add_alt', views.add_alt),
    url(r'^users_alt', views.users_alt),
    url(r'^delete_alt/(?P<email_id>\w+)$', views.delete_alt)
]
