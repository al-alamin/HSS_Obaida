# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('download_center', '0004_auto_20161020_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='download_link',
            field=models.URLField(unique=True),
        ),
    ]
