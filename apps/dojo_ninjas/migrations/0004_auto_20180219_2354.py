# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-19 23:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas', '0003_auto_20180219_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ninja',
            name='dojo',
            field=models.ForeignKey(db_column='attended_dojo_id', on_delete=django.db.models.deletion.CASCADE, related_name='ninjas', to='dojo_ninjas.Dojo'),
        ),
    ]
