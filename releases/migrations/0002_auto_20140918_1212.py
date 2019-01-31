# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('releases', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='release',
            name='development',
        ),
        migrations.AddField(
            model_name='release',
            name='has_ovf_package',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='release',
            name='beta_ovf_url',
            field=models.URLField(help_text='If this is a beta release, specify a direct download link to virtual appliance.', blank=True),
        ),
        migrations.AlterField(
            model_name='release',
            name='source_url',
            field=models.URLField(help_text='Direct download link to source code', blank=True),
        ),
    ]
