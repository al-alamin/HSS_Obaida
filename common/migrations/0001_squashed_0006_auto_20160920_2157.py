# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    replaces = [('common', '0001_initial'), ('common', '0002_auto_20160818_0052'), ('common', '0003_auto_20160919_1107'), ('common', '0004_auto_20160919_1152'), ('common', '0005_auto_20160919_1508'), ('common', '0006_auto_20160920_2157')]

    dependencies = [
        ('event', '0004_auto_20160919_1107'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('text', models.TextField(max_length=500)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('url', models.URLField(null=True, blank=True)),
                ('short_bio', models.TextField(null=True, blank=True, max_length=200)),
                ('long_bio', models.TextField(null=True, blank=True, max_length=5000)),
                ('facebook_link', models.URLField(null=True, blank=True)),
                ('linkedin_link', models.URLField(null=True, blank=True)),
                ('twitter_link', models.URLField(null=True, blank=True)),
                ('gplus_link', models.URLField(null=True, blank=True)),
                ('thumbnail', models.ImageField(upload_to='images/', default='images/user_default.jpg')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField(max_length=5000)),
                ('date', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(to='common.Author')),
                ('category', models.ManyToManyField(to='common.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('text', models.TextField(max_length=500)),
                ('date', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(to='common.Author')),
                ('category', models.ManyToManyField(to='common.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(help_text='parent category for category and tag. eg, Visa, Higher Study', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='tag',
            name='type',
            field=models.ForeignKey(to='common.Type', blank=True),
        ),
        migrations.AddField(
            model_name='question',
            name='tag',
            field=models.ManyToManyField(to='common.Tag', blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(to='common.Tag', blank=True),
        ),
        migrations.AddField(
            model_name='category',
            name='type',
            field=models.ForeignKey(to='common.Type', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='author',
            name='role',
            field=models.ManyToManyField(to='common.AuthorRole'),
        ),
        migrations.AddField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(to='common.Author'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.OneToOneField(to='common.Question'),
        ),
        migrations.AlterOrderWithRespectTo(
            name='answer',
            order_with_respect_to='question',
        ),
        migrations.CreateModel(
            name='UserMeta',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('url', models.URLField(null=True, blank=True)),
                ('short_bio', models.TextField(null=True, blank=True, max_length=200)),
                ('long_bio', models.TextField(null=True, blank=True, max_length=5000)),
                ('facebook_link', models.URLField(null=True, blank=True)),
                ('linkedin_link', models.URLField(null=True, blank=True)),
                ('twitter_link', models.URLField(null=True, blank=True)),
                ('gplus_link', models.URLField(null=True, blank=True)),
                ('thumbnail', models.ImageField(upload_to='images/', default='images/user_default.jpg')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
