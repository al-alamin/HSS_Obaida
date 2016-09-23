# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160920_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured_img',
            field=models.ImageField(upload_to='images/blog/', default='images/blog/img22.jpg', help_text='This image will be used in item blog page'),
        ),
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(upload_to='images/blog/', default='images/blog/img22.jpg', help_text='This image will be used in blog page or as a thumbnail in sidebar'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.CharField(max_length=30, choices=[('blog', 'blog'), ('news', 'news'), ('other', 'other')]),
        ),
    ]
