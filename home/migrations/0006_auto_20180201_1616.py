# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-01 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20180201_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='registration_fee',
            field=models.IntegerField(),
        ),
    ]
