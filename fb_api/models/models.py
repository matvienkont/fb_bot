from django.db import models
from django.utils import timezone


class Message(models.Model):
    message = models.TextField(blank=False, unique=False)
    created_at = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=30, unique=False, blank=True)