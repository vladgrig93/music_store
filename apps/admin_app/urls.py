from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^admin_portal$', views.index),
    url(r'^addrecord$', views.addrecord),
    url(r'^proccess_record$', views.proccess_record),
    url(r'^record_page/(?P<record_id>\d+)', views.record_page)
    ]
    