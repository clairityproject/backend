from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from django.forms.widgets import Select, CheckboxSelectMultiple
from django.forms.extras.widgets import SelectDateWidget
from data.models import Node


class ClarityForm(forms.Form):
  def addError(self, message):
    self._errors[NON_FIELD_ERRORS] = self.error_class([message])
    
class DownloadForm(ClarityForm):
    nodes_raw = Node.objects.values_list('node_id','name')
    node_choices = tuple([(a,(a,b)) for (a,b) in nodes_raw])

    nodes = forms.MultipleChoiceField(
            choices=nodes_raw,
            widget  = forms.CheckboxSelectMultiple,
            )
