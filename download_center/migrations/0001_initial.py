# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('degree', models.CharField(max_length=20, choices=[('MS', 'MS'), ('PhD', 'PhD')])),
                ('comment', models.CharField(max_length=500)),
                ('download_link', models.URLField()),
                ('department', models.ForeignKey(to='download_center.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=25, help_text='e,g; SOP, Resume, Mail, Others')),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='type',
            field=models.ForeignKey(to='download_center.Type'),
        ),
    ]
