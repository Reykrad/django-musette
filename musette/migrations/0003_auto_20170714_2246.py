# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-15 01:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musette', '0002_profile_receiveemails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ReceiveEmails',
            field=models.BooleanField(default=True, help_text='If receive Emails', verbose_name='Receive Emails'),
        ),
    ]
