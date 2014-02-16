# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Deleting model 'Url'
        db.delete_table(u'poolWatchApp_url')

        # Adding model 'UrlStack'
        db.create_table(u'poolWatchApp_urlstack', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length='400')),
            ('processed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('multiPool', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'poolWatchApp', ['UrlStack'])


    def backwards(self, orm):
        # Adding model 'Url'
        db.create_table(u'poolWatchApp_url', (
            ('url', self.gf('django.db.models.fields.URLField')(max_length='400')),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'poolWatchApp', ['Url'])

        # Deleting model 'UrlStack'
        db.delete_table(u'poolWatchApp_urlstack')


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
            'responseErr': ('django.db.models.fields.CharField', [], {'max_length': '5000', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': "'250'"}),
            'urljson': ('django.db.models.fields.URLField', [], {'max_length': "'400'", 'blank': 'True'}),
            'urlstats': ('django.db.models.fields.URLField', [], {'max_length': "'400'", 'blank': 'True'})
        },
        u'poolWatchApp.urlstack': {
            'Meta': {'object_name': 'UrlStack'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'multiPool': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'processed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': "'400'"})
        }
    }

    complete_apps = ['poolWatchApp']