from django import forms
from .models import Pet

# Form for creating and updating pet records
class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'species', 'breed', 'age', 'gender', 'description', 'image', 'adoption_status', 'suburb', 'state', 'adoption_fee']

# Form for searching pets
class PetSearchForm(forms.Form):
    # Form fields with optional filtering options for pet search
    species = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    breed = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(choices=[('', 'Any')] + Pet.GENDER_CHOICES, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    adoption_fee = forms.DecimalField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    suburb = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    state = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
