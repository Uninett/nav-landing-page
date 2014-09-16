# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Release.release_date'
        db.add_column(u'releases_release', 'release_date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 9, 2, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Release.release_date'
        db.delete_column(u'releases_release', 'release_date')


    models = {
        u'releases.release': {
            'Meta': {'object_name': 'Release'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'release_date': ('django.db.models.fields.DateField', [], {}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['releases']