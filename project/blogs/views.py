# -*- coding=utf8 -*-
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from .models import Record
from .forms import RecordForm
from users.models import Users

class RecordListView(ListView):
    model = Record
    context_object_name = 'records'

    def get_queryset(self):
        pk_list = [self.kwargs.get('pk', None)]
        if not pk_list[0]:
            pk_list = [self.request.user.id]
            try:
                subscribes = self.request.user.users.subscribes.all().values_list('id', flat=True)
                pk_list.extend(list(subscribes))
            except AttributeError:
                pass
        queryset = Record.objects.filter(creator_id__in=list(pk_list))
        return queryset

    def get_context_data(self, **kwargs):
        context = super(RecordListView, self).get_context_data(**kwargs)
        try:
            context['title'] = Users.objects.get(id=self.kwargs['pk']).blog_name
        except KeyError:
            context['title'] = 'Лента новостей'
        return context

class RecordDetailView(DetailView):
    model = Record
    context_object_name = 'record'

class RecordCreateView(LoginRequiredMixin, CreateView):
    form_class = RecordForm
    template_name = 'blogs/add_record.html'

    def form_valid(self, form):
        self.instance = form.save(commit=False)
        self.instance.creator = self.request.user.users
        self.instance.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return self.instance.get_absolute_url


