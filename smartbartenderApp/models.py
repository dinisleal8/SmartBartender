from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    CATEGORY_CHOICES = [
        ('admin', 'Admin'),
        ('guest', 'Guest'),
    ]
    category = models.CharField(max_length=5, choices=CATEGORY_CHOICES, default='guest')
