# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-12 15:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('talent', '0002_auto_20170412_1511'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='is_confirmed',
            new_name='is_verified',
        ),
    ]
