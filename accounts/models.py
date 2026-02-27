from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    ROLE_CHOICES = (
        ('job_seeker', 'Job Seeker'),
        ('recruiter', 'Recruiter'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='job_seeker'
    )

    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )

    profile_completed = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.username
        