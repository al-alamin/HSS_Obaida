# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20160922_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='featured_img',
            field=models.ImageField(help_text='This image will be used in single blog page', default='images/blog/img22.jpg', upload_to='images/blog/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(max_length=50000),
        ),
    ]
