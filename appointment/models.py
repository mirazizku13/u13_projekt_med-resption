from django.db import models

from doctors.models import Doctor
from patients.models import Patient


# Create your models here.
class appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    comment = models.TextField()