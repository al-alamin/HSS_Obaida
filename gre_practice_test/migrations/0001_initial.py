# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-20 13:13
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GreMCQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_type', models.CharField(choices=[(1, 'Comparison Question'), (2, 'One Answer Question'), (3, 'Multiple Answer Question'), (4, 'Numeric Entry Question')], help_text='Select MCQ Type: ', max_length=30)),
                ('question', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Question')),
                ('choice_a', models.CharField(blank=True, max_length=200, null=True)),
                ('choice_b', models.CharField(blank=True, max_length=200, null=True)),
                ('choice_c', models.CharField(blank=True, max_length=200, null=True)),
                ('choice_d', models.CharField(blank=True, max_length=200, null=True)),
                ('choice_e', models.CharField(blank=True, max_length=200, null=True)),
                ('choice_f', models.CharField(blank=True, max_length=200, null=True)),
                ('answer', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=3), size=None)),
                ('answer_explanation', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Answer Explanation: ')),
                ('difficulty', models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='GreModelTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('fee', models.PositiveSmallIntegerField(default=0)),
                ('difficulty', models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='GreModelTestResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_time', models.DateTimeField(blank=True, null=True)),
                ('marks', models.IntegerField(default=0)),
                ('model_test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gre_practice_test.GreModelTest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GreSubjectTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('subject_type', models.CharField(choices=[('quantitative', 'Quantitative Reasoning'), ('verbal', 'Verbal Reasoning'), ('analytical', 'Analytical Writing')], help_text='Select Subject Type: ', max_length=30)),
                ('fee', models.PositiveSmallIntegerField(default=0)),
                ('duration', models.PositiveSmallIntegerField(default=30)),
                ('per_mcq_marks', models.PositiveSmallIntegerField(default=1)),
                ('difficulty', models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1)),
                ('model_test', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gre_practice_test.GreModelTest')),
            ],
        ),
        migrations.CreateModel(
            name='GreSubjestTestResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_time', models.DateTimeField(blank=True, null=True)),
                ('marks', models.IntegerField(default=0)),
                ('user_answers', django.contrib.postgres.fields.ArrayField(base_field=models.PositiveSmallIntegerField(), blank=True, null=True, size=None)),
                ('subject_test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gre_practice_test.GreSubjectTest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='gremcq',
            name='subject_test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gre_practice_test.GreSubjectTest'),
        ),
    ]
