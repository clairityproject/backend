# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Node'
        db.create_table(u'data_node', (
            ('node_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('latitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('longitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('added_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('indoor', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'data', ['Node'])

        # Adding model 'Latest'
        db.create_table(u'data_latest', (
            ('node_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('indoor', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('latitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('longitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('temperature', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('rh', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dylos_bin_1', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dylos_bin_2', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dylos_bin_3', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dylos_bin_4', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('alphasense_1', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('alphasense_2', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('alphasense_3', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('alphasense_4', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('alphasense_5', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('alphasense_6', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('alphasense_7', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('alphasense_8', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('added_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'data', ['Latest'])

        # Adding model 'DataPoint'
        db.create_table(u'data_datapoint', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('node_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('temperature', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('rh', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dylos_bin_1', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dylos_bin_2', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dylos_bin_3', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dylos_bin_4', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('alphasense_1', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('alphasense_2', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('alphasense_3', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('alphasense_4', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('alphasense_5', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('alphasense_6', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('alphasense_7', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('alphasense_8', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('added_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('reading_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'data', ['DataPoint'])

        # Adding model 'Dylos'
        db.create_table(u'data_dylos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('node_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('dylos_bin_1', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dylos_bin_2', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dylos_bin_3', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dylos_bin_4', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('added_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('reading_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'data', ['Dylos'])

        # Adding model 'Alphasense'
        db.create_table(u'data_alphasense', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('node_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('alphasense_1', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('alphasense_2', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('alphasense_3', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('alphasense_4', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('alphasense_5', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('alphasense_6', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('alphasense_7', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('alphasense_8', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('added_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('reading_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'data', ['Alphasense'])

        # Adding model 'Met'
        db.create_table(u'data_met', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('node_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('temperature', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('rh', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('added_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('reading_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'data', ['Met'])

        # Adding model 'AQI'
        db.create_table(u'data_aqi', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('node_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('no', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('no2', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('o3', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('co', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dylos_bin_1', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dylos_bin_2', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dylos_bin_3', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dylos_bin_4', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('mitaqi', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('no_rank', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('no2_rank', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('o3_rank', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('co_rank', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('dylos_bin_1_rank', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('dylos_bin_2_rank', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('dylos_bin_3_rank', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('dylos_bin_4_rank', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('mitaqi_rank', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('added_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'data', ['AQI'])

        # Adding model 'SensorDetail'
        db.create_table(u'data_sensordetail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('node_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('no_serial', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('o3_serial', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('no2_serial', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('co_serial', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('no_electronic_we_zero', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('no_total_we_zero', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('no_electronic_aux_zero', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('no_total_aux_zero', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('no_electronic_we_sens', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('no_total_we_sens', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('o3_electronic_we_zero', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('o3_total_we_zero', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('o3_electronic_aux_zero', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('o3_total_aux_zero', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('o3_electronic_we_sens', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('o3_total_we_sens', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('no2_electronic_we_zero', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('no2_total_we_zero', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('no2_electronic_aux_zero', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('no2_total_aux_zero', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('no2_electronic_we_sens', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('no2_total_we_sens', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('co_electronic_we_zero', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('co_total_we_zero', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('co_electronic_aux_zero', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('co_total_aux_zero', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('co_electronic_we_sens', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('co_total_we_sens', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'data', ['SensorDetail'])


    def backwards(self, orm):
        # Deleting model 'Node'
        db.delete_table(u'data_node')

        # Deleting model 'Latest'
        db.delete_table(u'data_latest')

        # Deleting model 'DataPoint'
        db.delete_table(u'data_datapoint')

        # Deleting model 'Dylos'
        db.delete_table(u'data_dylos')

        # Deleting model 'Alphasense'
        db.delete_table(u'data_alphasense')

        # Deleting model 'Met'
        db.delete_table(u'data_met')

        # Deleting model 'AQI'
        db.delete_table(u'data_aqi')

        # Deleting model 'SensorDetail'
        db.delete_table(u'data_sensordetail')


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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'node_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'reading_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'data.aqi': {
            'Meta': {'object_name': 'AQI'},
            'added_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'co': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'co_rank': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dylos_bin_1': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dylos_bin_1_rank': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dylos_bin_2': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dylos_bin_2_rank': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dylos_bin_3': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dylos_bin_3_rank': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dylos_bin_4': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dylos_bin_4_rank': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'mitaqi': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mitaqi_rank': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'no': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'no2': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'no2_rank': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'no_rank': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'node_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'o3': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'o3_rank': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
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
            'dylos_bin_1': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dylos_bin_2': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dylos_bin_3': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dylos_bin_4': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'node_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'reading_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
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