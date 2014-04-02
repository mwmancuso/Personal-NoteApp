# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tokens'
        db.create_table('authentication_tokens', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('purpose', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('token', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('exhausted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('expiration', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('authentication', ['Tokens'])

        # Adding field 'Methods.expiration'
        db.add_column('authentication_methods', 'expiration',
                      self.gf('django.db.models.fields.DateTimeField')(null=True),
                      keep_default=False)

        # Deleting field 'Users.validated'
        db.delete_column('authentication_users', 'validated')


    def backwards(self, orm):
        # Deleting model 'Tokens'
        db.delete_table('authentication_tokens')

        # Deleting field 'Methods.expiration'
        db.delete_column('authentication_methods', 'expiration')

        # Adding field 'Users.validated'
        db.add_column('authentication_users', 'validated',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    models = {
        'authentication.methods': {
            'Meta': {'object_name': 'Methods'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'expiration': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_used': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'method': ('django.db.models.fields.IntegerField', [], {}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'step': ('django.db.models.fields.IntegerField', [], {}),
            'token': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['authentication.Users']"})
        },
        'authentication.tokens': {
            'Meta': {'object_name': 'Tokens'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'exhausted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'expiration': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'purpose': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'authentication.users': {
            'Meta': {'object_name': 'Users'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_access': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'user_type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['authentication']