# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0012_auto_20161028_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='calendar_invitation_link',
            field=models.TextField(null=True, blank=True),
        ),
    ]
