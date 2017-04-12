# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-12 20:59
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='talent',
            name='max_number_student',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(9), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='talent',
            name='min_number_student',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(9), django.core.validators.MinValueValidator(1)]),
        ),
    ]
