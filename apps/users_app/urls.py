from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^user_portal$', views.index),
    url(r'^viewcart$', views.viewcart),
    url(r'^category$', views.category),
    url(r'^artist$', views.artist),
    url(r'^search$', views.search)]
