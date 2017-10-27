from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^user_portal$', views.index),
    url(r'^viewcart$', views.viewcart),
    url(r'^category/(?P<artist_record_genre>\w+)$', views.category),
    url(r'^artist/(?P<artist_id>\d+)$', views.artist),
    url(r'^record/(?P<artist_record_id>\d+)$', views.record),
    url(r'^settings$', views.settings),
    url(r'^artist$', views.artist),
    url(r'^addrecord$', views.addrecord),
    url(r'^search$', views.search),
    url(r'^removeitem$', views.removeitem),
    url(r'cart$',views.displaycart),
    url(r'displayconfirmation$',views.display_confirmation),
    url(r'processpayment$',views.processpayment)]
