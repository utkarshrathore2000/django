from django import forms
from newapp.models import details
class employeform(forms.ModelForm):
    class Meta:
        model=details
        fields='__all__'
