from django.contrib import admin
from data.models import  Node, DataPoint, Dylos, Alphasense, Met, Latest, SensorDetail
import csv
from django.core.exceptions import PermissionDenied
from django.http import StreamingHttpResponse
import itertools
from datetime import datetime
class Echo(object):
    """An object that implements just the write method of the file-like
    interface.
    """
    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value

def export_as_csv(modeladmin, request, queryset):
    """
    Generic csv export admin action.
    """
    opts = modeladmin.model._meta
    field_names = [field.verbose_name for field in opts.fields]

    def csvgen():
            yield writer.writerow(field_names)
            gen = (writer.writerow([getattr(obj, field) for field in field_names]) for obj in queryset.iterator())
            for row in gen:
                yield row


    #if not request.user.is_staff:
        #raise PermissionDenied

    pseudo_buffer = Echo()
    writer = csv.writer(pseudo_buffer)
    # Write a first row with header information
    # Write data rows

    response = StreamingHttpResponse(csvgen(), content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=%s-%s.csv' % (unicode(opts).replace('.', '_'), str(datetime.now()).replace(' ','_'))

    return response

export_as_csv.short_description = "Export selected objects as csv file"



# Register your models here.


class BaseAdmin(admin.ModelAdmin):
    actions = [export_as_csv]
    list_filter = ('added_on','node_id')


class  LatestAdmin(BaseAdmin):
    list_display = ['node_id',
            'name',
            'indoor',
            'latitude',
            'longitude',
            'temperature',
            'rh',
            'no',
            'no2',
            'o3',
            'co',
            'last_modified']
    list_filter = ('last_modified','indoor')

class DylosAdmin(BaseAdmin):
    list_display = ('node_id','dylos_bin_1','dylos_bin_2','dylos_bin_3','dylos_bin_4', 'reading_time', 'added_on')

class AlphasenseAdmin(BaseAdmin):
    list_display = ('node_id', 'alphasense_1', 'alphasense_2', 'alphasense_3',
            'alphasense_4', 'alphasense_5', 'alphasense_6', 'alphasense_7', 'alphasense_8', 'reading_time', 'added_on')

class MetAdmin(BaseAdmin):
    list_display = ('node_id', 'rh', 'temperature', 'reading_time', 'added_on')

class NodeAdmin(BaseAdmin):
    list_display = ('node_id','name','indoor', 'latitude', 'longitude')

class SensorDetailAdmin(admin.ModelAdmin):
    list_display = ('node_id',)

admin.site.register(Node, NodeAdmin)
#admin.site.register(DataPoint, BaseAdmin)
#admin.site.register(AQI, BaseAdmin)
admin.site.register(SensorDetail, SensorDetailAdmin)

admin.site.register(Dylos, DylosAdmin)
admin.site.register(Alphasense, AlphasenseAdmin)
admin.site.register(Met, MetAdmin)

admin.site.register(Latest, LatestAdmin)
