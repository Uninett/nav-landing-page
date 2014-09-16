# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Release.beta'
        db.add_column(u'releases_release', 'beta',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Release.development'
        db.add_column(u'releases_release', 'development',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Release.beta'
        db.delete_column(u'releases_release', 'beta')

        # Deleting field 'Release.development'
        db.delete_column(u'releases_release', 'development')


    models = {
        u'releases.release': {
            'Meta': {'ordering': "['-release_date']", 'object_name': 'Release'},
            'beta': ('django.db.models.fields.BooleanField', [], {}),
            'development': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'release_date': ('django.db.models.fields.DateField', [], {}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['releases']