# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'School'
        db.create_table(u'location_school', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['location.Department'])),
        ))
        db.send_create_signal(u'location', ['School'])

        # Adding model 'Department'
        db.create_table(u'location_department', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['location.Country'], blank=True)),
        ))
        db.send_create_signal(u'location', ['Department'])

        # Adding model 'Country'
        db.create_table(u'location_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
        ))
        db.send_create_signal(u'location', ['Country'])


    def backwards(self, orm):
        # Deleting model 'School'
        db.delete_table(u'location_school')

        # Deleting model 'Department'
        db.delete_table(u'location_department')

        # Deleting model 'Country'
        db.delete_table(u'location_country')


    models = {
        u'location.country': {
            'Meta': {'object_name': 'Country'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'})
        },
        u'location.department': {
            'Meta': {'object_name': 'Department'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['location.Country']", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'location.school': {
            'Meta': {'object_name': 'School'},
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['location.Department']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        }
    }

    complete_apps = ['location']