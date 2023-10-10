# forms.py
from django import forms
from .models import Shelter

class ShelterForm(forms.ModelForm):
    class Meta:
        model = Shelter
        fields = ['shelter_name', 'address', 'phone_number', 'contact_email']
