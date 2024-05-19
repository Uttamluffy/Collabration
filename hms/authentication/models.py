# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('tutor', ('Tutor')),
        ('student', ('Student')),
        ('admin', ('Admin')),
    )
    
    first_name = models.CharField(max_length=20, blank=False, null=False)
    last_name = models.CharField(max_length=20, blank=False, null=False)

    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='student')
    
    def __str__(self):
        return self.username
    
    def get_full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'