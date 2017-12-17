#-*- encoding: utf8 -*-
from django.db import models
from django.contrib.auth.models import User
from blogs.models import Record

class Users(models.Model):
    user = models.OneToOneField(User, null=True)
    blog_name = models.CharField(max_length=200, blank=True, verbose_name='Название блога')
    subscribes = models.ManyToManyField('Users', related_name='subscribers', verbose_name='Подписки', blank=True)
    viewed_records = models.ManyToManyField(Record, related_name='viewers', verbose_name='Просмотренные', blank=True)

    @property
    def get_viewed_ids(self):
        ids =self.viewed_records.all().values_list('id', flat=True)
        return list(ids)

    def __str__(self):
        return self.user.get_full_name()