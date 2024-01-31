from django import forms
from . models import *

class Manage_form(forms.ModelForm):
    class Meta:
        model=Manage
        fields='__all__'