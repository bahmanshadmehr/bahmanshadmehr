# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 01:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emailgatherer', '0007_auto_20170903_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='join',
            name='ref_id',
            field=models.CharField(max_length=120),
        ),
    ]