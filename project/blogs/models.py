#-*- encoding: utf8 -*-
from django.db import models
from users.models import Users

class Record(models.Model):
    creator = models.ForeignKey(Users, related_name='records', verbose_name='Автор')
    title = models.CharField(max_length=200, blank=True, verbose_name='Название')
    body = models.TextField(verbose_name='Текст')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

class ViewedRecords(models.Model):
    record = models.ForeignKey(Record, related_name='viewers',verbose_name='Запись', on_delete=models.CASCADE)
    user = models.ForeignKey(Users, related_name='viewed_records', verbose_name='Читатель', on_delete=models.CASCADE)