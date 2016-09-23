# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160922_1723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='date_modified',
        ),
        migrations.AddField(
            model_name='post',
            name='date_created',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2016, 9, 22, 22, 43, 30, 819666, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
