# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('releases', '0002_auto_20140918_1212'),
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('series', models.CharField(help_text='The series number, e.g. 4.1', max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='release',
            options={'ordering': ['release_date']},
        ),
        migrations.AddField(
            model_name='release',
            name='series',
            field=models.ForeignKey(related_name=b'releases', default=1, to='releases.Series'),
            preserve_default=False,
        ),
    ]
