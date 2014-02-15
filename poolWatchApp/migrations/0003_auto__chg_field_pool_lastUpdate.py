# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Pool.lastUpdate'
        db.alter_column(u'poolWatchApp_pool', 'lastUpdate', self.gf('django.db.models.fields.DateTimeField')(null=True))

    def backwards(self, orm):

        # Changing field 'Pool.lastUpdate'
        db.alter_column(u'poolWatchApp_pool', 'lastUpdate', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 15, 0, 0)))

    models = {
        u'poolWatchApp.currency': {
            'Meta': {'object_name': 'Currency'},
            'cdif': ('django.db.models.fields.FloatField', [], {'default': '0', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'shortname': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        },
        u'poolWatchApp.pool': {
            'Meta': {'object_name': 'Pool'},
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['poolWatchApp.Currency']"}),
            'dateCreate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastUpdate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pageLoad': ('django.db.models.fields.FloatField', [], {'default': '0', 'blank': 'True'}),
            'poolEfficiency': ('django.db.models.fields.FloatField', [], {'default': '0', 'blank': 'True'}),
            'poolHashRate': ('django.db.models.fields.FloatField', [], {'default': '0', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': "'250'"}),
            'urljson': ('django.db.models.fields.URLField', [], {'max_length': "'400'", 'blank': 'True'}),
            'urlstats': ('django.db.models.fields.URLField', [], {'max_length': "'400'", 'blank': 'True'})
        }
    }

    complete_apps = ['poolWatchApp']