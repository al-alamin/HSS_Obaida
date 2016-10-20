# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('download_center', '0003_auto_20161020_1430'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='document',
            options={'ordering': ['-id']},
        ),
    ]
