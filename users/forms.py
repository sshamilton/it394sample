from .models import Cadet, Company
from django import forms

class CadetForm(forms.ModelForm):
    class Meta:
        model = Cadet
        fields = '__all__'


