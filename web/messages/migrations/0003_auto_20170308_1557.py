# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-08 15:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messages', '0002_auto_20170307_1332'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='conversation',
            options={'ordering': ['latest_message__sent_at']},
        ),
    ]
