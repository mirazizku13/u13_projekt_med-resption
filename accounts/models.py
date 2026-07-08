from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Username o'rniga telefon raqamidan foydalanamiz
    phone_number = models.CharField(max_length=15, unique=True)

    # Foydalanuvchi rollari
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('patient' , 'Patient')
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Patient')

    USERNAME_FIELD = 'phone_number'   # Tizimga kirish
    REQUIRED_FIELDS = ['username']  # Django superuser yaratishda so'raladigan maydon

    def __str__(self):
        return f"{self.first_name} {self.last_name} : Phone Number ({self.phone_number})"


