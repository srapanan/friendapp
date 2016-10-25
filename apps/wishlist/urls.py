from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^addproduct$', views.addproduct, name="addproduct"),
    url(r'^createproduct$', views.createproduct, name="createproduct"),
    url(r'^show/(?P<id>\d+)$', views.show, name="show"),
    url(r'^delete/(?P<id>\d+)$', views.delete, name="delete"),
    url(r'^remove/(?P<id>\d+)$', views.remove, name="remove"),
    url(r'^join/(?P<id>\d+)$', views.join, name="join"),
]
