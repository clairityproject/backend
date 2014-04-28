#!/usr/bin/env python
import csv
from data.models import SensorDetail

# load csv
sensors = []

for s in csv.reader(open('sensor_details.csv')):
    try:
        int(s[0])
    except:
        continue

    try:
        sensor = SensorDetail()
        sensor.node_id = int(s[0])
        sensor.no_serial = s[1]
        sensor.o3_serial = s[2]
        sensor.no2_serial = s[3]
        sensor.co_serial = s[4]

        sensor.no_electronic_we_zero  = int(s[5])
        sensor.no_total_we_zero   = int(s[6])
        sensor.no_electronic_aux_zero  = int(s[7])
        sensor.no_total_aux_zero  = int(s[8])
        sensor.no_electronic_we_sens = int(s[9])
        sensor.no_total_we_sens = float(s[10])

        sensor.o3_electronic_we_zero = int(s[11])
        sensor.o3_total_we_zero = int(s[12])
        sensor.o3_electronic_aux_zero = int(s[13])
        sensor.o3_total_aux_zero  = int(s[14])
        sensor.o3_electronic_we_sens = int(s[15])
        sensor.o3_total_we_sens = float(s[16])

        sensor.no2_electronic_we_zero = int(s[17])
        sensor.no2_total_we_zero = int(s[18])
        sensor.no2_electronic_aux_zero = int(s[19])
        sensor.no2_total_aux_zero  = int(s[20])
        sensor.no2_electronic_we_sens = int(s[21])
        sensor.no2_total_we_sens = float(s[22])

        sensor.co_electronic_we_zero = int(s[23])
        sensor.co_total_we_zero = int(s[24])
        sensor.co_electronic_aux_zero = int(s[25])
        sensor.co_total_aux_zero  = int(s[26])
        sensor.co_electronic_we_sens = int(s[27])
        sensor.co_total_we_sens = float(s[28])

        sensor.save()
        sensors.append(sensor)
    except Exception as e:
        print "Error occurred "
        print e.message
