# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0009_auto_20161001_0855'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('task_name', models.CharField(unique=True, max_length=50)),
                ('task_id', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='TaskId',
        ),
    ]
