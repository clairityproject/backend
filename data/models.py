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
    offline = models.BooleanField(default=False)

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

    big_particles = models.IntegerField(blank=True, null=True)
    small_particles = models.IntegerField(blank=True, null=True)

    no = models.FloatField(blank=True, null=True)
    no2 = models.FloatField(blank=True, null=True)
    co = models.FloatField(blank=True, null=True)
    o3 = models.FloatField(blank=True, null=True)

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
    dylos_bin_1 = models.IntegerField(blank=True, null=True)
    dylos_bin_2 = models.IntegerField(blank=True, null=True)
    dylos_bin_3 = models.IntegerField(blank=True, null=True)
    dylos_bin_4 = models.IntegerField(blank=True, null=True)

    big_particles = models.IntegerField(blank=True, null=True)
    small_particles = models.IntegerField(blank=True, null=True)

    added_on = models.DateTimeField(auto_now_add=True, db_index=True)
    last_modified = models.DateTimeField(auto_now_add=True, auto_now=True)
    reading_time = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return str(self.node_id) + ", " + str([self.dylos_bin_1 , self.dylos_bin_2, self.dylos_bin_3, self.dylos_bin_4])

    def save(self, *args, **kwargs):
        self.small_particles = int(self.dylos_bin_1) + int(self.dylos_bin_2) + int(self.dylos_bin_3)
        self.big_particles = int(self.dylos_bin_4)
        super(Dylos, self).save(*args, **kwargs)


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

    no = models.FloatField(blank=True, null=True, verbose_name="NO (ppb)")
    no2 = models.FloatField(blank=True, null=True, verbose_name="NO2 (ppb)")
    co = models.FloatField(blank=True, null=True, verbose_name="CO (ppb)")
    o3 = models.FloatField(blank=True, null=True, verbose_name="O3 (ppb)")

    added_on = models.DateTimeField(auto_now_add=True, db_index=True)
    last_modified = models.DateTimeField(auto_now_add=True, auto_now=True)
    reading_time = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return str(self.node_id) + ", " + str([self.alphasense_1, self.alphasense_2, self.alphasense_3, self.alphasense_4, self.alphasense_5, self.alphasense_6, self.alphasense_7, self.alphasense_8])

    def save(self, *args, **kwargs):
        try:
            sd = SensorDetail.objects.get(node_id=int(self.node_id))
            # no
            self.no = ((float(self.alphasense_1)- sd.no_electronic_we_zero) - (float(self.alphasense_2)- sd.no_electronic_aux_zero))/sd.no_total_we_sens
            self.no = float(self.no) * 1000
            # o3
            self.o3 = ((float(self.alphasense_3)- sd.o3_electronic_we_zero) - (float(self.alphasense_4)- sd.o3_electronic_aux_zero))/sd.o3_total_we_sens
            self.o3 = float(self.o3) * 1000
            # co
            self.co = ((float(self.alphasense_5)- sd.co_electronic_we_zero) - (float(self.alphasense_6)- sd.co_electronic_aux_zero))/sd.co_total_we_sens
            self.co = float(self.co) * 1000
            # no2
            self.no2 = ((float(self.alphasense_7)- sd.no2_electronic_we_zero) - (float(self.alphasense_8)- sd.no2_electronic_aux_zero))/sd.no2_total_we_sens
            self.no2 = float(self.no2) * 1000
        except Exception as e:
            print "ERROR saving alpha-sense : node_id = ", self.node_id
            print str(e)
            pass
        super(Alphasense, self).save(*args, **kwargs)

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
    no2_total_we_zero = models.IntegerField(blank=True, null=True) # use this
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
