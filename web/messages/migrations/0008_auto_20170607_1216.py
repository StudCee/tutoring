# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-07 12:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messages', '0007_auto_20170607_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.TextField(default=''),
        ),
    ]
