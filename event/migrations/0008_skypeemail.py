# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_auto_20160920_2157'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkypeEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_subject', models.CharField(max_length=100)),
                ('email_body', ckeditor.fields.RichTextField(max_length=500)),
                ('event', models.ForeignKey(to='event.Event')),
            ],
        ),
    ]
