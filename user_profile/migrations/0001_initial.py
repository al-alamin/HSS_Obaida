# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0007_auto_20160929_2045')
    ]

    state_operations = [
        migrations.CreateModel(
            name='UserMeta',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('url', models.URLField(null=True, blank=True)),
                ('short_bio', models.TextField(null=True, blank=True, max_length=200)),
                ('long_bio', models.TextField(null=True, blank=True, max_length=5000)),
                ('facebook_link', models.URLField(null=True, blank=True)),
                ('linkedin_link', models.URLField(null=True, blank=True)),
                ('twitter_link', models.URLField(null=True, blank=True)),
                ('gplus_link', models.URLField(null=True, blank=True)),
                ('thumbnail', models.ImageField(default='images/user_default.jpg', upload_to='images/')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
    operations = [
        migrations.SeparateDatabaseAndState(state_operations=state_operations)
    ]