# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-01 15:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20180201_1555'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='registration',
            new_name='registration_fee',
        ),
    ]
