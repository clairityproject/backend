from django.contrib import admin
from data.models import  Node, DataPoint, AQI, Dylos, Alphasense, Met, Latest
import csv
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse

def export_as_csv(modeladmin, request, queryset):
    """
    Generic csv export admin action.
    """
    if not request.user.is_staff:
        raise PermissionDenied
    opts = modeladmin.model._meta
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=%s.csv' % unicode(opts).replace('.', '_')
    writer = csv.writer(response)
    field_names = [field.name for field in opts.fields]
    # Write a first row with header information
    writer.writerow(field_names)
    # Write data rows
    for obj in queryset:
        writer.writerow([getattr(obj, field) for field in field_names])
    return response
export_as_csv.short_description = "Export selected objects as csv file"



# Register your models here.


class BaseAdmin(admin.ModelAdmin):
    actions = [export_as_csv]
    list_filter = ('added_on',)

admin.site.register(Node, BaseAdmin)
admin.site.register(DataPoint, BaseAdmin)
admin.site.register(AQI, BaseAdmin)

admin.site.register(Dylos, BaseAdmin)
admin.site.register(Alphasense, BaseAdmin)
admin.site.register(Met, BaseAdmin)

admin.site.register(Latest, BaseAdmin)
