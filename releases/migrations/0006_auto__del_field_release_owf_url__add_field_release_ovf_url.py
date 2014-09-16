# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Release.owf_url'
        db.delete_column(u'releases_release', 'owf_url')

        # Adding field 'Release.ovf_url'
        db.add_column(u'releases_release', 'ovf_url',
                      self.gf('django.db.models.fields.URLField')(default='http://nav.uninett.no', max_length=200),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Release.owf_url'
        raise RuntimeError("Cannot reverse this migration. 'Release.owf_url' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Release.owf_url'
        db.add_column(u'releases_release', 'owf_url',
                      self.gf('django.db.models.fields.URLField')(max_length=200),
                      keep_default=False)

        # Deleting field 'Release.ovf_url'
        db.delete_column(u'releases_release', 'ovf_url')


    models = {
        u'releases.release': {
            'Meta': {'ordering': "['-release_date']", 'object_name': 'Release'},
            'beta': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'development': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ovf_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'release_date': ('django.db.models.fields.DateField', [], {}),
            'source_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['releases']