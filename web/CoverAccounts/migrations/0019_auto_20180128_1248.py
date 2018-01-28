# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-28 12:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoverAccounts', '0018_auto_20180124_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='covermember',
            name='telegram_bot_token',
            field=models.CharField(default=None, help_text=b'You can setup the "CACTuS Messenger" bot in Telegram. The bot will ask you for this code.', max_length=160, verbose_name=b'Telegram Bot Token'),
        ),
        migrations.AddField(
            model_name='covermember',
            name='telegram_chat_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='covermember',
            name='telegram_id_counter',
            field=models.IntegerField(default=0),
        ),
    ]