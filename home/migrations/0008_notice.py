# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-01 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20180201_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'', max_length=300)),
                ('notice', models.CharField(default=b'', max_length=5000)),
            ],
        ),
    ]
