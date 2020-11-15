from django.db import models
from django.utils import timezone

class Message(models.Model):

    REVIEW = 'To be reviewed'
    PROGRESS = 'In progress'
    COMPLETED = 'Completed'
    CLOSED = 'Closed'
    STATUSES = [
        (REVIEW, 'To be reviewed'),
        (PROGRESS, 'In progress'),
        (COMPLETED, 'Completed'),
        (CLOSED, 'Closed')
    ]

    message = models.TextField(blank=False, unique=False)
    created_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=15,
        choices=STATUSES,
        default=REVIEW,
    )
    author_id = models.CharField(max_length=50, blank=False)
    author = models.CharField(max_length=30, unique=False, blank=True)
    response_message = models.TextField(blank=True, unique=False)
    message_id = models.CharField(max_length=50)
