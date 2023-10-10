# forms.py
from django import forms
from .models import AdoptionApplication

class AdoptionApplicationFormUser(forms.ModelForm):
    class Meta:
        model = AdoptionApplication
        fields = ['adopter_comments']


class AdoptionApplicationForm(forms.ModelForm):
    class Meta:
        model = AdoptionApplication
        fields = ['manager_comments']

