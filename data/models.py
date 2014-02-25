from django.db import models

# Create your models here.
class IP(models.Model):
    node = models.ForeignKey('Node')
    address = models.IPAddressField(null=True, blank=True)
    added_on = models.DateTimeField(auto_now_add=True)

class Node(models.Model):
    location = models.ForeignKey('Location')
    number = models.IntegerField(blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now_add=True, auto_now=True)
    ip = models.ForeignKey(IP)
 
class DataPoint(models.Model):
    node = models.ForeignKey(Node)
    temperature = models.FloatField(null=True, blank=True)
    # relative humidity
    rh = models.FloatField(null=True, blank=True) 
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


