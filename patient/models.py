from django.db import models

class Patient(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    telephone_number = models.IntegerField()
    email = models.EmailField()
    description = models.TextField()
    times = models.IntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
# Create your models here.
