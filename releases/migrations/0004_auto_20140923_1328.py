# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('releases', '0003_auto_20140918_1350'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='release',
            options={},
        ),
        migrations.RemoveField(
            model_name='release',
            name='series',
        ),
        migrations.DeleteModel(
            name='Series',
        ),
    ]
