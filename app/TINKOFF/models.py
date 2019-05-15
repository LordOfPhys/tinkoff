# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique = True, verbose_name = 'user', related_name = 'my_profile')
    phone = models.CharField(max_length = 30, default = 'Телефон')
    email = models.EmailField(max_length = 100, default = 'eMail')
    name = models.CharField(max_length = 100, default = 'ФИО')
    Type_gr = (
               ('Director', 'Директор'),
               ('Employee', 'Сотрудник'),
    )
    power = models.CharField(max_length = 30, choices = Type_gr, default = 'Должность')
    def __unicode__(self):
        return self.user.username
