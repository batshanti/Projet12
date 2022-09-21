from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    TEAM = [
        ('manager', 'manager'),
        ('sales', 'sales'),
        ('support', 'support')
    ]

    team = models.CharField(max_length=10, choices=TEAM)
