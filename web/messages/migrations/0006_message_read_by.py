# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-07 07:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('messages', '0005_auto_20170308_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='read_by',
            field=models.ManyToManyField(blank=True, related_name='read_messages', to=settings.AUTH_USER_MODEL),
        ),
    ]
