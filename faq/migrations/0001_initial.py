# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-05 15:26
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500)),
                ('ans', ckeditor.fields.RichTextField(blank=True, max_length=1500)),
                ('is_popular', models.BooleanField(default=False)),
                ('date_modified', models.DateField(auto_now=True)),
                ('category', models.ManyToManyField(to='common.Category')),
                ('tag', models.ManyToManyField(blank=True, to='common.Tag')),
            ],
        ),
    ]
