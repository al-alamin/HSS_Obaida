# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0011_event_calendar_invitation_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='calendar_invitation_link',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
    ]
