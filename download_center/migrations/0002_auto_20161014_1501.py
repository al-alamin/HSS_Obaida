# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('download_center', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='document',
            name='comment',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='document',
            name='degree',
            field=models.CharField(choices=[('Undergrad', 'Undergrad'), ('Masters', 'Masters'), ('PhD', 'PhD')], max_length=20),
        ),
        migrations.AlterField(
            model_name='type',
            name='name',
            field=models.CharField(max_length=25, unique=True, help_text='e,g; SOP, Resume, Mail, Others'),
        ),
    ]
