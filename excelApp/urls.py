from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path("", views.index, name="index"),
    url(r'^search/$', views.search),
    url(r'^search-form/$', views.index),

]