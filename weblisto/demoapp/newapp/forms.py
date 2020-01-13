from django import forms
from newapp.models import Employee
class employeform(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'
