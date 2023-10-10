from django import forms
from .models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'species', 'breed', 'age', 'gender', 'description', 'image', 'adoption_status', 'suburb', 'state', 'adoption_fee', 'shelter', 'adopter']  # Include desired fields
