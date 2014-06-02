# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Student'
        db.create_table(u'student_student', (
            (u'person_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['person.Person'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'student', ['Student'])


    def backwards(self, orm):
        # Deleting model 'Student'
        db.delete_table(u'student_student')


    models = {
        u'person.person': {
            'Meta': {'object_name': 'Person'},
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'serial': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'student.student': {
            'Meta': {'object_name': 'Student', '_ormbases': [u'person.Person']},
            u'person_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['person.Person']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['student']