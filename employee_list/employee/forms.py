from django import forms
from django.forms import ModelForm 

from .models import *

class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = {'Full_name','mobile','emp_code','Position'}
        labels = {
            'Full_name': 'Full_Name',
            'emp_code' : 'EMP.code'
        }