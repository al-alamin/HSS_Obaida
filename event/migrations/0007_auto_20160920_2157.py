# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_remove_event_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='presenter',
            field=models.ForeignKey(help_text="Presenter should have 'usermeta' data.", to=settings.AUTH_USER_MODEL),
        ),
    ]
