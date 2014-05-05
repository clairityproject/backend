# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'AQI'
        db.delete_table(u'data_aqi')

        # Adding field 'Dylos.big_particles'
        db.add_column(u'data_dylos', 'big_particles',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Dylos.small_particles'
        db.add_column(u'data_dylos', 'small_particles',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


        # Changing field 'Dylos.dylos_bin_3'
        db.alter_column(u'data_dylos', 'dylos_bin_3', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Dylos.dylos_bin_4'
        db.alter_column(u'data_dylos', 'dylos_bin_4', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Dylos.dylos_bin_1'
        db.alter_column(u'data_dylos', 'dylos_bin_1', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Dylos.dylos_bin_2'
        db.alter_column(u'data_dylos', 'dylos_bin_2', self.gf('django.db.models.fields.IntegerField')(null=True))
        # Adding field 'Alphasense.no'
        db.add_column(u'data_alphasense', 'no',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Alphasense.no2'
        db.add_column(u'data_alphasense', 'no2',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Alphasense.co'
        db.add_column(u'data_alphasense', 'co',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Alphasense.o3'
        db.add_column(u'data_alphasense', 'o3',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'AQI'
        db.create_table(u'data_aqi', (
            ('co', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('mitaqi', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dylos_bin_3_rank', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('dylos_bin_4_rank', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('no_rank', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('no2', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dylos_bin_2_rank', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('no', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('co_rank', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('dylos_bin_4', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('o3', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dylos_bin_3', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dylos_bin_2', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('o3_rank', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('node_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('mitaqi_rank', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('dylos_bin_1_rank', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('dylos_bin_1', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('no2_rank', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('added_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True, db_index=True)),
        ))
        db.send_create_signal(u'data', ['AQI'])

        # Deleting field 'Dylos.big_particles'
        db.delete_column(u'data_dylos', 'big_particles')

        # Deleting field 'Dylos.small_particles'
        db.delete_column(u'data_dylos', 'small_particles')


        # Changing field 'Dylos.dylos_bin_3'
        db.alter_column(u'data_dylos', 'dylos_bin_3', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Dylos.dylos_bin_4'
        db.alter_column(u'data_dylos', 'dylos_bin_4', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Dylos.dylos_bin_1'
        db.alter_column(u'data_dylos', 'dylos_bin_1', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Dylos.dylos_bin_2'
        db.alter_column(u'data_dylos', 'dylos_bin_2', self.gf('django.db.models.fields.FloatField')(null=True))
        # Deleting field 'Alphasense.no'
        db.delete_column(u'data_alphasense', 'no')

        # Deleting field 'Alphasense.no2'
        db.delete_column(u'data_alphasense', 'no2')

        # Deleting field 'Alphasense.co'
        db.delete_column(u'data_alphasense', 'co')

        # Deleting field 'Alphasense.o3'
        db.delete_column(u'data_alphasense', 'o3')


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
            'indoor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'node_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_index': 'True'}),
            'rh': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
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
            'node_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_index': 'True'})
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