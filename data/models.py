from django.db import models

# Create your models here.
class IP(models.Model):
    node_number = models.IntegerField(null=True, blank=True)
    address = models.IPAddressField(null=True, blank=True)
    added_on = models.DateTimeField(auto_now_add=True)

class Node(models.Model):
    location = models.ForeignKey('Location')
    number = models.IntegerField(blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now_add=True, auto_now=True)
    ip = models.ForeignKey('IP')

class Location(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

class DataPoint(models.Model):
    #node = models.ForeignKey(Node)
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
    reading_time = models.DateTimeField(blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now_add=True, auto_now=True)

class Dylos(models.Model):
    node_id = models.IntegerField(blank=False, null=False)
    dylos_bin_1 = models.FloatField(blank=True, null=True)
    dylos_bin_2 = models.FloatField(blank=True, null=True)
    dylos_bin_3 = models.FloatField(blank=True, null=True)
    dylos_bin_4 = models.FloatField(blank=True, null=True)
    reading_time = models.DateTimeField(blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now_add=True, auto_now=True)

class Alphasense(models.Model):
    node_id = models.IntegerField(blank=False, null=False)
    alphasense_1 = models.FloatField(blank=True, null=True)
    alphasense_2 = models.FloatField(blank=True, null=True)
    alphasense_3 = models.FloatField(blank=True, null=True)
    alphasense_4 = models.FloatField(blank=True, null=True)
    alphasense_5 = models.FloatField(blank=True, null=True)
    alphasense_6 = models.FloatField(blank=True, null=True)
    alphasense_7 = models.FloatField(blank=True, null=True)
    alphasense_8 = models.FloatField(blank=True, null=True)
    reading_time = models.DateTimeField(blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now_add=True, auto_now=True)


class Met(models.Model):
    ## This is the meteorological class
    node_id = models.IntegerField(blank=False, null=False)
    temperature = models.FloatField(null=True, blank=True)
    rh = models.FloatField(null=True, blank=True) # relative humidity
    reading_time = models.DateTimeField(blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now_add=True, auto_now=True)

