# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-01-12 09:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('singer', '0003_auto_20190112_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performance',
            name='Venue',
            field=models.CharField(max_length=100),
        ),
    ]
