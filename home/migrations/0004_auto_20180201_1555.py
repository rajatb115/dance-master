# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-01 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20180201_1554'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='course_etails',
        ),
        migrations.AddField(
            model_name='registration',
            name='course_dtails',
            field=models.CharField(default=b'', max_length=5000),
        ),
        migrations.AlterField(
            model_name='registration',
            name='course_name',
            field=models.CharField(default=b'', max_length=300),
        ),
    ]
