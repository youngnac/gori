# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-27 07:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='talent',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]
