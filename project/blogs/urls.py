from django.conf.urls import url
from .views import RecordListView, RecordDetailView, RecordCreateView, mark_viewed

urlpatterns = [
    url(r'^$', RecordListView.as_view(), name='records'),
    url(r'^(?P<pk>[0-9]+)/$', RecordListView.as_view(), name='records'),
    url(r'^record/(?P<pk>[0-9]+)/$', RecordDetailView.as_view(), name='record'),
    url(r'^record/(?P<pk>[0-9]+)/mark_viewed/$', mark_viewed, name='mark_viewed'),
    url(r'^add/$', RecordCreateView.as_view(), name='add_record')
]