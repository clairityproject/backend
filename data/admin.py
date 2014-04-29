from django.contrib import admin
from data.models import  Node, DataPoint, AQI, Dylos, Alphasense, Met, Latest
import csv
from django.core.exceptions import PermissionDenied
from django.http import StreamingHttpResponse

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
    print "Entering expoirt_as sc"
    print queryset.query
    if not request.user.is_staff:
        raise PermissionDenied
    opts = modeladmin.model._meta
    pseudo_buffer = Echo()
    writer = csv.writer(pseudo_buffer)
    field_names = [field.name for field in opts.fields]
    # Write a first row with header information
    writer.writerow(field_names)
    # Write data rows

    response = StreamingHttpResponse((writer.writerow([getattr(obj, field) for field in field_names]) for obj in queryset.iterator()),
            content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=%s.csv' % unicode(opts).replace('.', '_')

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
            'dylos_bin_1',   
            'dylos_bin_2',   
            'dylos_bin_3',   
            'dylos_bin_4',   
            'alphasense_1',  
            'alphasense_2',  
            'alphasense_3',  
            'alphasense_4',  
            'alphasense_5',  
            'alphasense_6',  
            'alphasense_7',  
            'alphasense_8',  
            'last_modified']
    list_filter = ('last_modified','indoor')


admin.site.register(Node, BaseAdmin)
admin.site.register(DataPoint, BaseAdmin)
admin.site.register(AQI, BaseAdmin)

admin.site.register(Dylos, BaseAdmin)
admin.site.register(Alphasense, BaseAdmin)
admin.site.register(Met, BaseAdmin)

admin.site.register(Latest, LatestAdmin)
