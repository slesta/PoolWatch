# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Currency'
        db.create_table(u'poolWatchApp_currency', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('shortname', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('cdif', self.gf('django.db.models.fields.FloatField')(default=1024, blank=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'poolWatchApp', ['Currency'])

        # Adding model 'Pool'
        db.create_table(u'poolWatchApp_pool', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('currency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['poolWatchApp.Currency'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('urlstats', self.gf('django.db.models.fields.URLField')(default=1024, max_length=200, blank=True)),
            ('urljson', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('pageLoad', self.gf('django.db.models.fields.FloatField')(default=1024, blank=True)),
            ('poolHashRate', self.gf('django.db.models.fields.FloatField')(default=1024, blank=True)),
            ('poolEfficiency', self.gf('django.db.models.fields.FloatField')(default=1024, blank=True)),
            ('dateCreate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('lastUpdate', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'poolWatchApp', ['Pool'])


    def backwards(self, orm):
        # Deleting model 'Currency'
        db.delete_table(u'poolWatchApp_currency')

        # Deleting model 'Pool'
        db.delete_table(u'poolWatchApp_pool')


    models = {
        u'poolWatchApp.currency': {
            'Meta': {'object_name': 'Currency'},
            'cdif': ('django.db.models.fields.FloatField', [], {'default': '1024', 'blank': 'True'}),
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
            'lastUpdate': ('django.db.models.fields.DateTimeField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pageLoad': ('django.db.models.fields.FloatField', [], {'default': '1024', 'blank': 'True'}),
            'poolEfficiency': ('django.db.models.fields.FloatField', [], {'default': '1024', 'blank': 'True'}),
            'poolHashRate': ('django.db.models.fields.FloatField', [], {'default': '1024', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'urljson': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'urlstats': ('django.db.models.fields.URLField', [], {'default': '1024', 'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['poolWatchApp']