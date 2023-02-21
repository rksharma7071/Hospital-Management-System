from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'dob', 'phone', 'email']

    name = forms.CharField(label='Name', max_length=255)
    dob = forms.DateField(label='Date of Birth')
    phone = forms.CharField(label='Phone', max_length=20)
    email = forms.EmailField(label='Email', max_length=255)