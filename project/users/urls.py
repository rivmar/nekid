from django.conf.urls import url
from .views import BlogsListView, subscribe, mark_viewed

urlpatterns = [
    url(r'^$', BlogsListView.as_view(), name='blogs'),
    url(r'^(?P<pk>[0-9]+)/subscribe/$', subscribe, name='subscribe'),
    url(r'^record/(?P<pk>[0-9]+)/mark_viewed/$', mark_viewed, name='mark_viewed'),
]