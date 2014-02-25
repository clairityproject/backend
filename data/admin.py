from django.contrib import admin
from data.models import IP, Node, Location, DataPoint

# Register your models here.

admin.site.register(IP)
admin.site.register(Node)
admin.site.register(Location)
