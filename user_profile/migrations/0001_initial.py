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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('url', models.URLField(blank=True, null=True)),
                ('short_bio', ckeditor.fields.RichTextField(max_length=400)),
                ('long_bio', ckeditor.fields.RichTextField(blank=True, max_length=5000, null=True)),
                ('facebook_link', models.URLField(blank=True, null=True)),
                ('linkedin_link', models.URLField(blank=True, null=True)),
                ('twitter_link', models.URLField(blank=True, null=True)),
                ('gplus_link', models.URLField(blank=True, null=True)),
                ('thumbnail', models.ImageField(default='images/user_default.jpg', upload_to='images/')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
