# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-20 17:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20180220_1724'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='description',
            new_name='desc',
        ),
    ]
