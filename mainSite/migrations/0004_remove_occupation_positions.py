# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-13 00:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainSite', '0003_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='occupation',
            name='positions',
        ),
    ]
