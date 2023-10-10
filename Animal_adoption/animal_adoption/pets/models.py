from django.db import models
from users.models import User
from shelters.models import Shelter  # Import Shelter model from the correct app

class Pet(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Unknown', 'Unknown'),
    ]

    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Unknown')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='pet_images/', blank=True)
    adoption_status = models.CharField(
        max_length=20,
        choices=[('Available', 'Available'), ('Pending', 'Pending'), ('Adopted', 'Adopted')],
        default='Available'
    )
    adoption_fee = models.DecimalField(max_digits=10, decimal_places=2)
    suburb = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=50, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    shelter = models.ForeignKey(Shelter, on_delete=models.SET_NULL, null=True, blank=True)
    adopter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name
