# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-14 07:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice_test', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subjesttestresult',
            old_name='myanswers',
            new_name='user_answers',
        ),
        migrations.RemoveField(
            model_name='modeltestresult',
            name='subject_wise_marks',
        ),
        migrations.AlterField(
            model_name='mcq',
            name='choice_a',
            field=models.CharField(default='a', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mcq',
            name='choice_b',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mcq',
            name='choice_c',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mcq',
            name='choice_d',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mcq',
            name='choice_e',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mcq',
            name='difficulty',
            field=models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1),
        ),
        migrations.AlterField(
            model_name='modeltest',
            name='difficulty',
            field=models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1),
        ),
        migrations.AlterField(
            model_name='subjecttest',
            name='difficulty',
            field=models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1),
        ),
    ]