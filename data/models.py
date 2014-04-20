from django.db import models

#------------------------------------------------------------
#    Base Classes
#------------------------------------------------------------

class Base(models.Model):
    added_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now_add=True, auto_now=True)

class BaseReading(Base):
    reading_time = models.DateTimeField(blank=True, null=True)

#------------------------------------------------------------
#    Utility Classes
#------------------------------------------------------------

class Node(models.Model):
    number = models.IntegerField(blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now_add=True, auto_now=True)
    ip_address = models.IPAddressField(null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

#------------------------------------------------------------
#    Data Classes
#------------------------------------------------------------

class DataPoint(BaseReading):
    node_id = models.IntegerField(blank=False, null=False)
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

class Dylos(BaseReading):
    node_id = models.IntegerField(blank=False, null=False)
    dylos_bin_1 = models.FloatField(blank=True, null=True)
    dylos_bin_2 = models.FloatField(blank=True, null=True)
    dylos_bin_3 = models.FloatField(blank=True, null=True)
    dylos_bin_4 = models.FloatField(blank=True, null=True)

class Alphasense(BaseReading):
    node_id = models.IntegerField(blank=False, null=False)
    alphasense_1 = models.FloatField(blank=True, null=True)
    alphasense_2 = models.FloatField(blank=True, null=True)
    alphasense_3 = models.FloatField(blank=True, null=True)
    alphasense_4 = models.FloatField(blank=True, null=True)
    alphasense_5 = models.FloatField(blank=True, null=True)
    alphasense_6 = models.FloatField(blank=True, null=True)
    alphasense_7 = models.FloatField(blank=True, null=True)
    alphasense_8 = models.FloatField(blank=True, null=True)


class Met(BaseReading):
    ## This is the meteorological class
    node_id = models.IntegerField(blank=False, null=False)
    temperature = models.FloatField(null=True, blank=True)
    rh = models.FloatField(null=True, blank=True) # relative humidity

class AQI(models.Model):
    """ This is where data is stored after processing"""
    node_id = models.IntegerField(blank=False, null=False)
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


