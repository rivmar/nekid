# -*- coding=utf8 -*-
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.core.mail import send_mass_mail
from django.conf import settings
from django.contrib.auth.models import AnonymousUser
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
                subscribes = self.request.user.subscribes.all().values_list('id', flat=True)
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
        self.instance.creator = self.request.user
        self.instance.save()
        self.send_email()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return self.instance.get_absolute_url

    def send_email(self):
        # move to form or sigmals
        host = self.request.META['HTTP_HOST']
        url = self.instance.get_absolute_url
        recipients = self.instance.creator.subscribers.all().values_list('email', flat=True)
        if recipients:
            send_mass_mail(
                'Новое сообщение в блоге',
                '''Пользователь {} опубликовал новую запись в своем блоге.
                Посмотреть запись: {}{}'''.format(self.instance.creator.get_full_name, host, url),
                settings.EMAIL_HOST_USER,
                recipients,
                fail_silently=False
            )

@login_required
def mark_viewed(request, pk):
    pass