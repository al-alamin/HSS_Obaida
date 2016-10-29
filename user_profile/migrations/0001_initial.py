# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMeta',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('url', models.URLField(null=True, blank=True)),
                ('short_bio', ckeditor.fields.RichTextField(max_length=400)),
                ('long_bio', ckeditor.fields.RichTextField(null=True, max_length=5000, blank=True)),
                ('facebook_link', models.URLField(null=True, blank=True)),
                ('linkedin_link', models.URLField(null=True, blank=True)),
                ('twitter_link', models.URLField(null=True, blank=True)),
                ('gplus_link', models.URLField(null=True, blank=True)),
                ('thumbnail', models.ImageField(upload_to='images/', default='images/user_default.jpg')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
