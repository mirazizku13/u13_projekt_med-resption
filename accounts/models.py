from django.contrib.auth.models import AbstractUser
from django.db import models

class Roles(models.TextChoices):
    ADMIN = "ADMIN", "Admin"
    Doctor = "Doctor", "Doctor"
    Patient = "Patient", "Patient"

class Profession(models.TextChoices):
    LOR = "LOR", "lor"
    THERAPIST = "THERAPIST", "therapist"
    SURGEON = "SURGEON", "surgeon"
    DENTIST = "DENTIST", "dentist"
    CARDIOLOGIST = "CARDIOLOGIST", "cardiologist"

class User(AbstractUser):
    phone_number = models.IntegerField()
    role = models.CharField(choices=Roles.choices, max_length=100, default=Roles.Patient)
    profession = models.CharField(
        max_length=100,
        choices=Profession.choices, null=True,
    )

    class Meta:
        db_table = 'users'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"