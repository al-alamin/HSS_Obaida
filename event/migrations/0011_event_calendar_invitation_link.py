# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0010_auto_20161020_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='calendar_invitation_link',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
