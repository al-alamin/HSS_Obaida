# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('download_center', '0002_auto_20161014_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='comment',
            field=ckeditor.fields.RichTextField(max_length=500, blank=True),
        ),
    ]
