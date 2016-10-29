# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_profile', '0002_auto_20161028_2246'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMeta',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('url', models.URLField(null=True, blank=True)),
                ('short_bio', ckeditor.fields.RichTextField(max_length=400)),
                ('long_bio', ckeditor.fields.RichTextField(null=True, max_length=5000, blank=True)),
                ('facebook_link', models.URLField(null=True, blank=True)),
                ('linkedin_link', models.URLField(null=True, blank=True)),
                ('twitter_link', models.URLField(null=True, blank=True)),
                ('gplus_link', models.URLField(null=True, blank=True)),
                ('thumbnail', models.ImageField(default='images/user_default.jpg', upload_to='images/')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
