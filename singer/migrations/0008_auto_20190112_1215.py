# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-01-12 12:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('singer', '0007_auto_20190112_0956'),
    ]

    operations = [
        migrations.AddField(
            model_name='instrumentalist',
            name='Song',
            field=models.ManyToManyField(to='singer.Song'),
        ),
        migrations.AddField(
            model_name='instrumentalist',
            name='Style',
            field=models.ManyToManyField(to='singer.Style'),
        ),
        migrations.AddField(
            model_name='performance',
            name='Song',
            field=models.ManyToManyField(to='singer.Song'),
        ),
        migrations.AddField(
            model_name='performance',
            name='Style',
            field=models.ManyToManyField(to='singer.Style'),
        ),
        migrations.AddField(
            model_name='song',
            name='Style',
            field=models.ManyToManyField(to='singer.Style'),
        ),
        migrations.AddField(
            model_name='vocalist',
            name='Song',
            field=models.ManyToManyField(to='singer.Song'),
        ),
        migrations.AddField(
            model_name='vocalist',
            name='Style',
            field=models.ManyToManyField(to='singer.Style'),
        ),
    ]
