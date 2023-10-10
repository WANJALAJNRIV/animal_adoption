from django import forms
from .models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'species', 'breed', 'age', 'gender', 'description', 'image', 'adoption_status', 'suburb', 'state', 'adoption_fee', 'shelter'] 



class PetSearchForm(forms.Form):
    species = forms.CharField(max_length=50, required=False)
    breed = forms.CharField(max_length=100, required=False)
    age = forms.IntegerField(required=False)
    gender = forms.ChoiceField(choices=[('', 'Any')] + Pet.GENDER_CHOICES, required=False)
    adoption_fee = forms.DecimalField(required=False)
    suburb = forms.CharField(max_length=100, required=False)
    state = forms.CharField(max_length=50, required=False)
