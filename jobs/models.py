from django.db import models
from django.conf import settings


class Job(models.Model):

    EXPERIENCE_CHOICES = (
        ('intern', 'Intern'),
        ('fresher', 'Fresher'),
        ('junior', 'Junior'),
        ('mid', 'Mid Level'),
        ('senior', 'Senior'),
        ('lead', 'Lead'),
    )

    title = models.CharField(max_length=255, db_index=True)

    description = models.TextField()

    salary = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True
    )

    location = models.CharField(max_length=255, db_index=True)

    experience_level = models.CharField(
        max_length=20,
        choices=EXPERIENCE_CHOICES,
        db_index=True
    )

    recruiter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='jobs'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['location']),
            models.Index(fields=['experience_level']),
        ]

    def __str__(self):
        return self.title