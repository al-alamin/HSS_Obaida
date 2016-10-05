# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celery_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasklist',
            old_name='task_id',
            new_name='celery_task_id',
        ),
        migrations.RenameField(
            model_name='tasklist',
            old_name='task_name',
            new_name='parent_task_name',
        ),
    ]
