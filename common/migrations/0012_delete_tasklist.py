# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0011_auto_20161001_0857'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TaskList',
        ),
    ]
