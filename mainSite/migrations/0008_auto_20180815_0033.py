# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-15 00:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainSite', '0007_auto_20180815_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='accomplishment',
            name='name',
            field=models.CharField(default='asefa', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='accomplishment',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]
