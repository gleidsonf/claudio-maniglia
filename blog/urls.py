from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='root_url'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post_by_type/(?P<pk>[0-9]+)/$', views.post_by_type, name='post_by_type'),
]
