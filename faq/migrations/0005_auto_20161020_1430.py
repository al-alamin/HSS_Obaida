# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0004_auto_20160920_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='ans',
            field=ckeditor.fields.RichTextField(max_length=1500, blank=True),
        ),
    ]
