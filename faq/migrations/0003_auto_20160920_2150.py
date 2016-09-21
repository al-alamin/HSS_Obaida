# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0002_auto_20160920_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='is_popular',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.ManyToManyField(to='common.Category'),
        ),
    ]
