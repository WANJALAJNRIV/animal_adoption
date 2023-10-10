from django.db import models

class Shelter(models.Model):
    shelter_name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    contact_email = models.EmailField()

    def __str__(self):
        return self.shelter_name
