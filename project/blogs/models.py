#-*- encoding: utf8 -*-
from django.db import models
from django.conf import settings
from django.urls import reverse

class Record(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='records', verbose_name='Автор')
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

class ViewedRecords(models.Model):
    record = models.ForeignKey(Record, related_name='viewers',verbose_name='Запись', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='viewed_records', verbose_name='Читатель', on_delete=models.CASCADE)