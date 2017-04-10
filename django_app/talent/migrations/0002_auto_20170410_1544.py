# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-10 06:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talent',
            name='category',
            field=models.CharField(choices=[('HNB', '헬스 / 뷰티'), ('LAN', '외국어'), ('COM', '컴퓨터'), ('ART', '미술 / 음악'), ('SPO', '스포츠'), ('JOB', '전공 / 취업'), ('HOB', '이색취미')], default='HNB', max_length=3),
        ),
    ]
