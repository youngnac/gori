# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-10 06:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20170410_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goriuser',
            name='profile_image',
            field=models.ImageField(blank=True, default='', upload_to='member/profile_image'),
        ),
    ]