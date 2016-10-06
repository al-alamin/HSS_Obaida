# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0010_auto_20161001_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='task_name',
            field=models.CharField(max_length=50),
        ),
    ]
