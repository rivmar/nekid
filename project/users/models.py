#-*- encoding: utf8 -*-
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Users(AbstractBaseUser):
    blog_name = models.CharField(max_length=200, blank=True, verbose_name='Название блога')
    subscribes = models.ManyToManyField('Users', related_name='subscribers', verbose_name='Подписчики')
