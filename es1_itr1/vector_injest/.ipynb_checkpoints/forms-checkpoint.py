from django import forms

from .models import DatasetUnit

class DatasetForm(forms.ModelForm):
    
    file = forms.FileField()
    
    class Meta:
        model = DatasetUnit
        fields = ['dataset_unit_name', 'dataset_unit_description']