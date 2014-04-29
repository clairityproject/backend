from django.db import models

#------------------------------------------------------------
#    Utility Classes
#------------------------------------------------------------

class Node(models.Model):
    node_id = models.IntegerField(primary_key=True, db_index=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now_add=True, auto_now=True)
    indoor = models.BooleanField(default=False)

    def __unicode__(self):
        return str(self.node_id) + " , " + self.name

class Latest(models.Model):
    node_id = models.IntegerField(primary_key=True, db_index=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    indoor = models.BooleanField(default=False)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    temperature = models.FloatField(null=True, blank=True)
    rh = models.FloatField(null=True, blank=True) # relative humidity

    dylos_bin_1 = models.FloatField(blank=True, null=True)
    dylos_bin_2 = models.FloatField(blank=True, null=True)
    dylos_bin_3 = models.FloatField(blank=True, null=True)
    dylos_bin_4 = models.FloatField(blank=True, null=True)

    alphasense_1 = models.FloatField(blank=True, null=True)
    alphasense_2 = models.FloatField(blank=True, null=True)
    alphasense_3 = models.FloatField(blank=True, null=True)
    alphasense_4 = models.FloatField(blank=True, null=True)
    alphasense_5 = models.FloatField(blank=True, null=True)
    alphasense_6 = models.FloatField(blank=True, null=True)
    alphasense_7 = models.FloatField(blank=True, null=True)
    alphasense_8 = models.FloatField(blank=True, null=True)

    added_on = models.DateTimeField(auto_now_add=True, db_index=True)
    last_modified = models.DateTimeField(auto_now_add=True, auto_now=True)

#------------------------------------------------------------
#    Data Classes
#------------------------------------------------------------

class DataPoint(models.Model):
    node_id = models.IntegerField(blank=False, null=False, db_index=True)
    temperature = models.FloatField(null=True, blank=True)
    rh = models.FloatField(null=True, blank=True) # relative humidity
    dylos_bin_1 = models.FloatField(blank=True, null=True)
    dylos_bin_2 = models.FloatField(blank=True, null=True)
    dylos_bin_3 = models.FloatField(blank=True, null=True)
    dylos_bin_4 = models.FloatField(blank=True, null=True)
    alphasense_1 = models.FloatField(blank=True, null=True)
    alphasense_2 = models.FloatField(blank=True, null=True)
    alphasense_3 = models.FloatField(blank=True, null=True)
    alphasense_4 = models.FloatField(blank=True, null=True)
    alphasense_5 = models.FloatField(blank=True, null=True)
    alphasense_6 = models.FloatField(blank=True, null=True)
    alphasense_7 = models.FloatField(blank=True, null=True)
    alphasense_8 = models.FloatField(blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add=True, db_index=True)
    last_modified = models.DateTimeField(auto_now_add=True, auto_now=True)
    reading_time = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return str(self.node_id) + " , " + str(self.reading_time)

class Dylos(models.Model):
    node_id = models.IntegerField(blank=False, null=False, db_index=True)
    dylos_bin_1 = models.FloatField(blank=True, null=True)
    dylos_bin_2 = models.FloatField(blank=True, null=True)
    dylos_bin_3 = models.FloatField(blank=True, null=True)
    dylos_bin_4 = models.FloatField(blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add=True, db_index=True)
    last_modified = models.DateTimeField(auto_now_add=True, auto_now=True)
    reading_time = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return str(self.node_id) + ", " + str([self.dylos_bin_1 , self.dylos_bin_2, self.dylos_bin_3, self.dylos_bin_4])

class Alphasense(models.Model):
    node_id = models.IntegerField(blank=False, null=False, db_index=True)
    alphasense_1 = models.FloatField(blank=True, null=True)
    alphasense_2 = models.FloatField(blank=True, null=True)
    alphasense_3 = models.FloatField(blank=True, null=True)
    alphasense_4 = models.FloatField(blank=True, null=True)
    alphasense_5 = models.FloatField(blank=True, null=True)
    alphasense_6 = models.FloatField(blank=True, null=True)
    alphasense_7 = models.FloatField(blank=True, null=True)
    alphasense_8 = models.FloatField(blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add=True, db_index=True)
    last_modified = models.DateTimeField(auto_now_add=True, auto_now=True)
    reading_time = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return str(self.node_id) + ", " + str([self.alphasense_1, self.alphasense_2, self.alphasense_3, self.alphasense_4, self.alphasense_5, self.alphasense_6, self.alphasense_7, self.alphasense_8]) 


class Met(models.Model):
    ## This is the meteorological class
    node_id = models.IntegerField(blank=False, null=False, db_index=True)
    temperature = models.FloatField(null=True, blank=True)
    rh = models.FloatField(null=True, blank=True) # relative humidity
    added_on = models.DateTimeField(auto_now_add=True, db_index=True)
    last_modified = models.DateTimeField(auto_now_add=True, auto_now=True)
    reading_time = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return str(self.node_id) + ", " + str([self.temperature , self.rh])

class AQI(models.Model):
    """ This is where data is stored after processing"""
    node_id = models.IntegerField(blank=False, null=False, db_index=True)
    no = models.FloatField(blank=True, null=True)
    no2 = models.FloatField(blank=True, null=True)
    o3 = models.FloatField(blank=True, null=True)
    co = models.FloatField(blank=True, null=True)
    dylos_bin_1 = models.FloatField(blank=True, null=True)
    dylos_bin_2 = models.FloatField(blank=True, null=True)
    dylos_bin_3 = models.FloatField(blank=True, null=True)
    dylos_bin_4 = models.FloatField(blank=True, null=True)
    mitaqi = models.FloatField(blank=True, null=True)
    no_rank = models.IntegerField(blank=True, null=True)
    no2_rank = models.IntegerField(blank=True, null=True)
    o3_rank = models.IntegerField(blank=True, null=True)
    co_rank = models.IntegerField(blank=True, null=True)
    dylos_bin_1_rank = models.IntegerField(blank=True, null=True)
    dylos_bin_2_rank = models.IntegerField(blank=True, null=True)
    dylos_bin_3_rank = models.IntegerField(blank=True, null=True)
    dylos_bin_4_rank = models.IntegerField(blank=True, null=True)
    mitaqi_rank = models.IntegerField(blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add=True, db_index=True)
    last_modified = models.DateTimeField(auto_now_add=True, auto_now=True)

    def __unicode__(self):
        return str(self.node_id) + ", " + self.mitaqi_rank


class SensorDetail(models.Model):
    node_id = models.IntegerField(blank=False, null=False, db_index=True)

    no_serial = models.CharField(max_length=200, blank=True, null=True)
    o3_serial = models.CharField(max_length=200, blank=True, null=True)
    no2_serial = models.CharField(max_length=200, blank=True, null=True)
    co_serial = models.CharField(max_length=200, blank=True, null=True)

    no_electronic_we_zero = models.IntegerField(blank=True, null=True)
    no_total_we_zero = models.IntegerField(blank=True, null=True)
    no_electronic_aux_zero = models.IntegerField(blank=True, null=True)
    no_total_aux_zero  = models.IntegerField(blank=True, null=True)
    no_electronic_we_sens = models.IntegerField(blank=True, null=True)
    no_total_we_sens = models.FloatField(blank=True, null=True)

    o3_electronic_we_zero = models.IntegerField(blank=True, null=True)
    o3_total_we_zero = models.IntegerField(blank=True, null=True)
    o3_electronic_aux_zero = models.IntegerField(blank=True, null=True)
    o3_total_aux_zero  = models.IntegerField(blank=True, null=True)
    o3_electronic_we_sens = models.IntegerField(blank=True, null=True)
    o3_total_we_sens = models.FloatField(blank=True, null=True)

    no2_electronic_we_zero = models.IntegerField(blank=True, null=True)
    no2_total_we_zero = models.IntegerField(blank=True, null=True)
    no2_electronic_aux_zero = models.IntegerField(blank=True, null=True)
    no2_total_aux_zero  = models.IntegerField(blank=True, null=True)
    no2_electronic_we_sens = models.IntegerField(blank=True, null=True)
    no2_total_we_sens = models.FloatField(blank=True, null=True)

    co_electronic_we_zero = models.IntegerField(blank=True, null=True)
    co_total_we_zero = models.IntegerField(blank=True, null=True)
    co_electronic_aux_zero = models.IntegerField(blank=True, null=True)
    co_total_aux_zero  = models.IntegerField(blank=True, null=True)
    co_electronic_we_sens = models.IntegerField(blank=True, null=True)
    co_total_we_sens = models.FloatField(blank=True, null=True)
