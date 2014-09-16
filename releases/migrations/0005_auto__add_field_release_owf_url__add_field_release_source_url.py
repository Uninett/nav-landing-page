# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Release.owf_url'
        db.add_column(u'releases_release', 'owf_url',
                      self.gf('django.db.models.fields.URLField')(default='http://nav.uninett.no', max_length=200),
                      keep_default=False)

        # Adding field 'Release.source_url'
        db.add_column(u'releases_release', 'source_url',
                      self.gf('django.db.models.fields.URLField')(default='http://nav.uninett.no', max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Release.owf_url'
        db.delete_column(u'releases_release', 'owf_url')

        # Deleting field 'Release.source_url'
        db.delete_column(u'releases_release', 'source_url')


    models = {
        u'releases.release': {
            'Meta': {'ordering': "['-release_date']", 'object_name': 'Release'},
            'beta': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'development': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owf_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'release_date': ('django.db.models.fields.DateField', [], {}),
            'source_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['releases']