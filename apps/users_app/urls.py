from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^user_portal$', views.index),
    url(r'^viewcart$', views.viewcart),
    url(r'^category$', views.category),
    url(r'^artist/(?P<artist_id>\d+)$', views.artist),
    url(r'^record/(?P<artist_record_id>\d+)$', views.record),]
    url(r'^settings$', views.settings),
    
]
