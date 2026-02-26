from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError


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

    company = models.ForeignKey(
        'companies.Company',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='recruiters'
    )

    def clean(self):
        if self.role == 'recruiter' and not self.company:
            raise ValidationError("Recruiter must belong to a company.")

    def __str__(self):
        return self.username
        