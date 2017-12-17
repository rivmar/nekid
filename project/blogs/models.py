#-*- encoding: utf8 -*-
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.db.models.signals import post_save
from django.core.mail import send_mass_mail

class Record(models.Model):
    creator = models.ForeignKey('users.Users', related_name='records', verbose_name='Автор')
    title = models.CharField(max_length=200, blank=True, verbose_name='Название')
    body = models.TextField(verbose_name='Текст')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

    @property
    def get_absolute_url(self):
        return reverse('blogs:record', kwargs={'pk':str(self.id)})

def record_created(sender,**kwargs):
    instance = kwargs.get('instance', None)
    created = kwargs.get('created', False)
    if created:
        host = settings.SITE_URL
        url = instance.get_absolute_url
        subscribers = instance.creator.subscribers.all()
        recipients = [s.user.email for s in subscribers]
        message = ('Новое сообщение в блоге',
                   '''Пользователь {} опубликовал новую запись в своем блоге.
                   Посмотреть запись: {}{}'''.format(instance.creator.user.get_full_name(), host, url),
                   settings.EMAIL_HOST_USER,
                   recipients),

        send_mass_mail(message, fail_silently=False)

post_save.connect(record_created, sender=Record)