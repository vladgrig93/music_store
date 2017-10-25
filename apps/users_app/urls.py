from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^user_portal$', views.index),]