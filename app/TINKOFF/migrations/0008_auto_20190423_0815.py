# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-04-23 08:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TINKOFF', '0007_auto_20190416_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='power',
            field=models.CharField(choices=[('1', '1'), ('2', '2')], default='\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c', max_length=30),
        ),
    ]