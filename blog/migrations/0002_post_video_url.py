# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-13 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='video_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]