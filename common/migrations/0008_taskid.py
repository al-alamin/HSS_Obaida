# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0007_auto_20160929_2045'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskId',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('task_id', models.CharField(max_length=50, unique=True)),
            ],
        ),
    ]
