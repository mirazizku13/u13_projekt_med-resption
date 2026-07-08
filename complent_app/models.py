from django.db import models

from patients.models import Patient


class Complent(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    decription = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient_id,self.decription

    class Meta:
        db_table = 'complent'

