# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Latest.offline'
        db.add_column(u'data_latest', 'offline',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Latest.offline'
        db.delete_column(u'data_latest', 'offline')


    models = {
        u'data.alphasense': {
            'Meta': {'object_name': 'Alphasense'},
            'added_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'alphasense_1': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'alphasense_2': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'alphasense_3': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'alphasense_4': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'alphasense_5': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'alphasense_6': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'alphasense_7': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'alphasense_8': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'co': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'no': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'no2': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'node_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'o3': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'reading_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'data.datapoint': {
            'Meta': {'object_name': 'DataPoint'},
            'added_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'alphasense_1': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'alphasense_2': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'alphasense_3': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'alphasense_4': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'alphasense_5': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'alphasense_6': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'alphasense_7': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'alphasense_8': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dylos_bin_1': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dylos_bin_2': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dylos_bin_3': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dylos_bin_4': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'node_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'reading_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'rh': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'temperature': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'data.dylos': {
            'Meta': {'object_name': 'Dylos'},
            'added_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'big_particles': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dylos_bin_1': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dylos_bin_2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dylos_bin_3': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dylos_bin_4': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'node_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'reading_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'small_particles': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'data.latest': {
            'Meta': {'object_name': 'Latest'},
            'added_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'big_particles': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'co': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'indoor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'no': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'no2': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'node_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_index': 'True'}),
            'o3': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'offline': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rh': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'small_particles': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'temperature': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'data.met': {
            'Meta': {'object_name': 'Met'},
            'added_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'node_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'reading_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'rh': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'temperature': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'data.node': {
            'Meta': {'object_name': 'Node'},
            'added_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'indoor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'node_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_index': 'True'}),
            'offline': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'data.sensordetail': {
            'Meta': {'object_name': 'SensorDetail'},
            'co_electronic_aux_zero': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'co_electronic_we_sens': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'co_electronic_we_zero': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'co_serial': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'co_total_aux_zero': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'co_total_we_sens': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'co_total_we_zero': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no2_electronic_aux_zero': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'no2_electronic_we_sens': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'no2_electronic_we_zero': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'no2_serial': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'no2_total_aux_zero': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'no2_total_we_sens': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'no2_total_we_zero': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'no_electronic_aux_zero': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'no_electronic_we_sens': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'no_electronic_we_zero': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'no_serial': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'no_total_aux_zero': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'no_total_we_sens': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'no_total_we_zero': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'node_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'o3_electronic_aux_zero': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'o3_electronic_we_sens': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'o3_electronic_we_zero': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'o3_serial': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'o3_total_aux_zero': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'o3_total_we_sens': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'o3_total_we_zero': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['data']