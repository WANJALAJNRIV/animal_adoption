from django.db import models

class AdoptionApplication(models.Model):
    applicant = models.ForeignKey('users.User', on_delete=models.CASCADE)
    pet = models.ForeignKey('pets.Pet', on_delete=models.CASCADE)
    application_status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')],
        default='Pending'
    )
    application_date = models.DateTimeField(auto_now_add=True)
    manager_comments = models.TextField(blank=True)
    adopter_inquiries = models.TextField(blank=True)
    last_updated = models.DateTimeField(auto_now=True)     
    residence_or_outdoor_space = models.TextField(blank=True)
    number_of_existing_pets = models.PositiveIntegerField(default=0, blank=True)
    pet_care_routine = models.TextField(blank=True)
    training_and_Socialization = models.TextField(blank=True)


    def __str__(self):
        return f"{self.applicant.username} - {self.pet.name}"

