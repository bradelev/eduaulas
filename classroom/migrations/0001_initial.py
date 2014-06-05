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
            ('escuela', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['location.School'])),
        ))
        db.send_create_signal(u'classroom', ['ClassRoom'])

        # Adding M2M table for field teachers on 'ClassRoom'
        m2m_table_name = db.shorten_name(u'classroom_classroom_teachers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('classroom', models.ForeignKey(orm[u'classroom.classroom'], null=False)),
            ('teacher', models.ForeignKey(orm[u'teacher.teacher'], null=False))
        ))
        db.create_unique(m2m_table_name, ['classroom_id', 'teacher_id'])

        # Adding model 'Grade'
        db.create_table(u'classroom_grade', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
        ))
        db.send_create_signal(u'classroom', ['Grade'])


    def backwards(self, orm):
        # Deleting model 'ClassRoom'
        db.delete_table(u'classroom_classroom')

        # Removing M2M table for field teachers on 'ClassRoom'
        db.delete_table(db.shorten_name(u'classroom_classroom_teachers'))

        # Deleting model 'Grade'
        db.delete_table(u'classroom_grade')


    models = {
        u'classroom.classroom': {
            'Meta': {'object_name': 'ClassRoom'},
            'class_letter': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '5', 'primary_key': 'True'}),
            'escuela': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['location.School']"}),
            'grade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['classroom.Grade']"}),
            'shift': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'teachers': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['teacher.Teacher']", 'symmetrical': 'False'})
        },
        u'classroom.grade': {
            'Meta': {'object_name': 'Grade'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
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
        },
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

    complete_apps = ['classroom']