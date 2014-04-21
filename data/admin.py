from django.contrib import admin
from data.models import  Node, DataPoint, AQI

# Register your models here.

admin.site.register(Node)
admin.site.register(DataPoint)
admin.site.register(AQI)
