from django.db import models
from accounts.models import User


class Doctor(models.Model):

    class Specialization(models.TextChoices):
            THERAPIST = "therapist", "Терапевт"
            CARDIOLOGIST = "cardiologist", "Кардиолог"
            SURGEON = "surgeon", "Хирург"
            PEDIATRICIAN = "pediatrician", "Педиатр"
            DERMATOLOGIST = "dermatologist", "Дерматолог"
            NEUROLOGIST = "neurologist", "Невролог"
            GYNECOLOGIST = "gynecologist", "Гинеколог"
            OPHTHALMOLOGIST = "ophthalmologist", "Офтальмолог"
            DENTIST = "dentist", "Стоматолог"
            ORTHOPEDIST = "orthopedist", "Ортопед"
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=30,choices=Specialization.choices,default=Specialization.THERAPIST)
    procedure_cost = models.DecimalField(max_digits=10, decimal_places=2)

