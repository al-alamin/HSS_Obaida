# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='date',
        ),
        migrations.AddField(
            model_name='post',
            name='date_modified',
            field=models.DateField(auto_now=True, default=datetime.datetime(2016, 9, 21, 2, 57, 20, 50156, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
