# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table(u'person_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('serial', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal(u'person', ['Person'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table(u'person_person')


    models = {
        u'person.person': {
            'Meta': {'object_name': 'Person'},
            'date_of_birth': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'serial': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        }
    }

    complete_apps = ['person']