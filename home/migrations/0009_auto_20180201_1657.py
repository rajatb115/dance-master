# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-01 16:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_notice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notice',
            old_name='notice',
            new_name='note',
        ),
    ]
