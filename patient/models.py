from django.db import models

from core import settings


class Status(models.TextChoices):
    Accept = 'Accept', 'accept'
    Refuse = 'Refuse', 'refuse'

class Patient(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    telephone_number = models.IntegerField()
    email = models.EmailField()
    description = models.TextField()
    times = models.IntegerField()
    # doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'role': 'Doctor'}, related_name='patients')
    status = models.CharField(max_length=11, choices=Status.choices,)
    message = models.TextField()


    class Meta:
        db_table = 'patient'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
# Create your models here.
