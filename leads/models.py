from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

STATUS = (
    ('Assigned', 'Assigned'),
    ('Unassigned', 'Unassigned'),
)

# Batch Model
class Lead(models.Model):
    agent = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    status = models.CharField(max_length=15, choices=STATUS, default='Unassigned', null=True)
    created_at = models.DateTimeField(
        null=True, blank=True, default=datetime.now)

    def __str__(self):
        return self.first_name

    def get_date(self):
        return self.created_at.date()

    class Meta:
        verbose_name_plural = "Leads"