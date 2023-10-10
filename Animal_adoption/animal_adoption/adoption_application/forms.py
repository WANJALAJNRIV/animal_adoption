# forms.py
from django import forms
from .models import AdoptionApplication

class AdoptionApplicationFormUser(forms.ModelForm):
    class Meta:
        model = AdoptionApplication
        fields = ['residence_or_outdoor_space','number_of_existing_pets','pet_care_routine','training_and_Socialization','adopter_inquiries']


class AdoptionApplicationForm(forms.ModelForm):
    class Meta:
        model = AdoptionApplication
        fields = ['manager_comments']

