from django.db import models

class Profession(models.TextChoices):
    LOR = "LOR", "LOR"
    THERAPIST = "THERAPIST", "Therapist"
    SURGEON = "SURGEON", "Surgeon"
    DENTIST = "DENTIST", "Dentist"
    CARDIOLOGIST = "CARDIOLOGIST", "Cardiologist"

class Doctors(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    profession = models.CharField(
        max_length=100,
        choices=Profession.choices
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"