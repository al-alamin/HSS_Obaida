# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_skypeemail'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventEmail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('email_subject', models.CharField(max_length=100)),
                ('email_body', ckeditor.fields.RichTextField(max_length=500)),
                ('event', models.ForeignKey(to='event.Event')),
            ],
        ),
        migrations.RemoveField(
            model_name='skypeemail',
            name='event',
        ),
        migrations.DeleteModel(
            name='SkypeEmail',
        ),
    ]
