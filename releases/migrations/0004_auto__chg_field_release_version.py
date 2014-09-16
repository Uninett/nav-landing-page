# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Release.version'
        db.alter_column(u'releases_release', 'version', self.gf('django.db.models.fields.CharField')(max_length=30))

    def backwards(self, orm):

        # Changing field 'Release.version'
        db.alter_column(u'releases_release', 'version', self.gf('django.db.models.fields.CharField')(max_length=10))

    models = {
        u'releases.release': {
            'Meta': {'ordering': "['-release_date']", 'object_name': 'Release'},
            'beta': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'development': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'release_date': ('django.db.models.fields.DateField', [], {}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['releases']