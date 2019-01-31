# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.CharField(help_text='This version number corresponds to for instance the doc folder name.', max_length=30)),
                ('release_date', models.DateField()),
                ('beta', models.BooleanField(default=False)),
                ('development', models.BooleanField(default=False)),
                ('beta_ovf_url', models.URLField(help_text='If this is a beta release, specify a direct download link to virtual appliance.')),
                ('source_url', models.URLField(help_text='Direct download link to source code')),
            ],
            options={
                'ordering': ['-release_date'],
            },
            bases=(models.Model,),
        ),
    ]
