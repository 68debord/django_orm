# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-20 02:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email_address',
            new_name='email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
        migrations.RemoveField(
            model_name='user',
            name='updated_at',
        ),
    ]
