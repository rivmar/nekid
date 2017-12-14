# -*- coding=utf8 -*-
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Record
from .forms import RecordForm

class RecordListView(ListView):
    model = Record
    context_object_name = 'records'

    def get_queryset(self):
        queryset = Record.objects.filter(creator_id=self.kwargs['pk'])
        return queryset

class FeedListView(LoginRequiredMixin, ListView):
    model = Record
    context_object_name = 'records'

    def get_queryset(self):
        queryset = Record.objects.filter(creator__in=self.request.user.subscribes)
        return queryset

class RecordCreateView(LoginRequiredMixin, CreateView):
    form_class = RecordForm

    def get_success_url(self):
        return 'oooops'

class RecordDetailView(DetailView):
    model = Record
    context_object_name = 'record'

@login_required
def mark_viewed(request, pk):
    pass

@login_required
def subscribe(request, pk):
    pass