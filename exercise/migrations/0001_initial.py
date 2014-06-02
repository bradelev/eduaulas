# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Result'
        db.create_table(u'exercise_result', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('points', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('answer', self.gf('django.db.models.fields.TextField')(null=True)),
            ('exercise', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['exercise.Exercise'])),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['student.Student'])),
            ('time_elapsed', self.gf('django.db.models.fields.IntegerField')(blank=True)),
        ))
        db.send_create_signal(u'exercise', ['Result'])

        # Adding model 'Exercise'
        db.create_table(u'exercise_exercise', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exercise_id', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('grade', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['classroom.Grade'])),
            ('topic', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['exercise.Topic'])),
            ('unit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['exercise.Unit'])),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('teacher_guide', self.gf('django.db.models.fields.TextField')(max_length=1000, blank=True)),
            ('img', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'exercise', ['Exercise'])

        # Adding M2M table for field good_related_exercises on 'Exercise'
        m2m_table_name = db.shorten_name(u'exercise_exercise_good_related_exercises')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_exercise', models.ForeignKey(orm[u'exercise.exercise'], null=False)),
            ('to_exercise', models.ForeignKey(orm[u'exercise.exercise'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_exercise_id', 'to_exercise_id'])

        # Adding M2M table for field bad_related_exercises on 'Exercise'
        m2m_table_name = db.shorten_name(u'exercise_exercise_bad_related_exercises')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_exercise', models.ForeignKey(orm[u'exercise.exercise'], null=False)),
            ('to_exercise', models.ForeignKey(orm[u'exercise.exercise'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_exercise_id', 'to_exercise_id'])

        # Adding model 'TeacherComments'
        db.create_table(u'exercise_teachercomments', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('teacher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teacher.Teacher'], blank=True)),
            ('comments', self.gf('django.db.models.fields.TextField')()),
            ('exercise', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['exercise.Exercise'])),
        ))
        db.send_create_signal(u'exercise', ['TeacherComments'])

        # Adding model 'Unit'
        db.create_table(u'exercise_unit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('letter', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=200, blank=True)),
            ('topic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['exercise.Topic'])),
            ('available', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'exercise', ['Unit'])

        # Adding model 'Area'
        db.create_table(u'exercise_area', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'exercise', ['Area'])

        # Adding model 'Topic'
        db.create_table(u'exercise_topic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'exercise', ['Topic'])


    def backwards(self, orm):
        # Deleting model 'Result'
        db.delete_table(u'exercise_result')

        # Deleting model 'Exercise'
        db.delete_table(u'exercise_exercise')

        # Removing M2M table for field good_related_exercises on 'Exercise'
        db.delete_table(db.shorten_name(u'exercise_exercise_good_related_exercises'))

        # Removing M2M table for field bad_related_exercises on 'Exercise'
        db.delete_table(db.shorten_name(u'exercise_exercise_bad_related_exercises'))

        # Deleting model 'TeacherComments'
        db.delete_table(u'exercise_teachercomments')

        # Deleting model 'Unit'
        db.delete_table(u'exercise_unit')

        # Deleting model 'Area'
        db.delete_table(u'exercise_area')

        # Deleting model 'Topic'
        db.delete_table(u'exercise_topic')


    models = {
        u'classroom.grade': {
            'Meta': {'object_name': 'Grade'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
        u'exercise.area': {
            'Meta': {'object_name': 'Area'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'exercise.exercise': {
            'Meta': {'object_name': 'Exercise'},
            'bad_related_exercises': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'bad_related_exercises_rel_+'", 'blank': 'True', 'to': u"orm['exercise.Exercise']"}),
            'exercise_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'good_related_exercises': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'good_related_exercises_rel_+'", 'blank': 'True', 'to': u"orm['exercise.Exercise']"}),
            'grade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['classroom.Grade']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'teacher_guide': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': u"orm['exercise.Topic']"}),
            'unit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['exercise.Unit']"})
        },
        u'exercise.result': {
            'Meta': {'object_name': 'Result'},
            'answer': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['exercise.Exercise']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'points': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['student.Student']"}),
            'time_elapsed': ('django.db.models.fields.IntegerField', [], {'blank': 'True'})
        },
        u'exercise.teachercomments': {
            'Meta': {'object_name': 'TeacherComments'},
            'comments': ('django.db.models.fields.TextField', [], {}),
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['exercise.Exercise']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teacher.Teacher']", 'blank': 'True'})
        },
        u'exercise.topic': {
            'Meta': {'object_name': 'Topic'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'exercise.unit': {
            'Meta': {'object_name': 'Unit'},
            'available': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'letter': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['exercise.Topic']"})
        },
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
        },
        u'teacher.teacher': {
            'Meta': {'object_name': 'Teacher', '_ormbases': [u'person.Person']},
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'person_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['person.Person']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['exercise']