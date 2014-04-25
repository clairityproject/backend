from django.contrib import admin
from data.models import  Node, DataPoint, AQI, Dylos, Alphasense, Met

# Register your models here.

admin.site.register(Node)
admin.site.register(DataPoint)
admin.site.register(AQI)

admin.site.register(Dylos)
admin.site.register(Alphasense)
admin.site.register(Met)
