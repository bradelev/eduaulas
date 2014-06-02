# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Student'
        db.create_table(u'student_student', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')()),
            ('gender', self.gf('django.db.models.fields.BooleanField')()),
            ('serial', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal(u'student', ['Student'])


    def backwards(self, orm):
        # Deleting model 'Student'
        db.delete_table(u'student_student')


    models = {
        u'student.student': {
            'Meta': {'object_name': 'Student'},
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'gender': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'serial': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        }
    }

    complete_apps = ['student']