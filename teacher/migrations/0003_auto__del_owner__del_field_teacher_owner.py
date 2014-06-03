# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Owner'
        db.delete_table(u'teacher_owner')

        # Deleting field 'Teacher.owner'
        db.delete_column(u'teacher_teacher', 'owner_id')


    def backwards(self, orm):
        # Adding model 'Owner'
        db.create_table(u'teacher_owner', (
            ('classroom', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['classroom.ClassRoom'])),
            ('is_owner', self.gf('django.db.models.fields.BooleanField')(default=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'teacher', ['Owner'])

        # Adding field 'Teacher.owner'
        db.add_column(u'teacher_teacher', 'owner',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=True, to=orm['teacher.Owner'], blank=True),
                      keep_default=False)


    models = {
        u'person.person': {
            'Meta': {'object_name': 'Person'},
            'date_of_birth': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'serial': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'teacher.teacher': {
            'Meta': {'object_name': 'Teacher', '_ormbases': [u'person.Person']},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'person_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['person.Person']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['teacher']