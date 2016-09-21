# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.ManyToManyField(help_text='**To make a question popular select "popular_faq" category.**', to='common.Category'),
        ),
        migrations.AlterField(
            model_name='question',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
