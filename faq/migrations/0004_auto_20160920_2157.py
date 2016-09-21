# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0003_auto_20160920_2150'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='date',
            new_name='date_modified',
        ),
    ]
