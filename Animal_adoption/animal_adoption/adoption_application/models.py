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
    adopter_comments = models.TextField(blank=True)


    def __str__(self):
        return f"{self.applicant.username} - {self.pet.name}"


