from django.conf.urls import url
from .views import BlogsListView, subscribe

urlpatterns = [
    url(r'^$', BlogsListView.as_view(), name='blogs'),
    url(r'^(?P<pk>[0-9]+)/subscribe/$', subscribe, name='subscribe'),
]