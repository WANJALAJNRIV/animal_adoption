# forms.py
from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        # Define which fields from the User model should be included in this form.
        fields = ['first_name', 'last_name','username', 'email', 'phone_number', 'address', 'role', 'password' ]  


class RegisterationForm(forms.ModelForm):
    class Meta:
        model = User
        # Define which fields from the User model should be included in this registration form.

        fields = ['first_name', 'last_name','username', 'email', 'phone_number', 'address',  'password' ]



from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        # Define which fields from the User model should be included in this authentication form.
        fields = ['username', 'password']

        
         