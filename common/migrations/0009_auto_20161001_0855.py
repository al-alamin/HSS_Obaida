# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0008_taskid'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskid',
            name='task_name',
            field=models.CharField(max_length=50, unique=True, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='taskid',
            name='task_id',
            field=models.CharField(max_length=50),
        ),
    ]
