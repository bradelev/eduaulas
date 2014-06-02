# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ClassRoom'
        db.create_table(u'classroom_classroom', (
            ('code', self.gf('django.db.models.fields.CharField')(max_length=5, primary_key=True)),
            ('class_letter', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('shift', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('grade', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['classroom.Grade'])),
        ))
        db.send_create_signal(u'classroom', ['ClassRoom'])

        # Adding model 'Grade'
        db.create_table(u'classroom_grade', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
        ))
        db.send_create_signal(u'classroom', ['Grade'])


    def backwards(self, orm):
        # Deleting model 'ClassRoom'
        db.delete_table(u'classroom_classroom')

        # Deleting model 'Grade'
        db.delete_table(u'classroom_grade')


    models = {
        u'classroom.classroom': {
            'Meta': {'object_name': 'ClassRoom'},
            'class_letter': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '5', 'primary_key': 'True'}),
            'grade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['classroom.Grade']"}),
            'shift': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'classroom.grade': {
            'Meta': {'object_name': 'Grade'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        }
    }

    complete_apps = ['classroom']