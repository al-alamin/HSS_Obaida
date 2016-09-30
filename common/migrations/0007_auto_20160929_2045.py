# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [('common','0006_auto_20160920_2157') ]


    database_operations = [
        migrations.AlterModelTable('UserMeta', 'user_profile_UserMeta')
    ]

    state_operations = [
        migrations.DeleteModel('UserMeta')
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=database_operations,
            state_operations=state_operations)
    ]