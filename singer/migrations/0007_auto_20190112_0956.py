# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-01-12 09:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('singer', '0006_auto_20190112_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performance',
            name='Date',
            field=models.CharField(max_length=100),
        ),
    ]
