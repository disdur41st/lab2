# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-10 18:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab2', '0002_auto_20160510_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='date',
            field=models.DateField(max_length=20),
        ),
    ]
