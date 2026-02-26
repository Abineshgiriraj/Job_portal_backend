# Create your models here.
from django.db import models
from django.conf import settings


class Company(models.Model):

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name