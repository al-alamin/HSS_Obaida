# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermeta',
            name='long_bio',
            field=ckeditor.fields.RichTextField(max_length=5000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='usermeta',
            name='short_bio',
            field=ckeditor.fields.RichTextField(default='shorbio', max_length=400),
            preserve_default=False,
        ),
    ]
