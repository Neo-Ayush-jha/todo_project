from django.db import models
from django.utils import timezone

class TodoItem(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('WORKING', 'Working'),
        ('DONE', 'Done'),
        ('OVERDUE', 'Overdue'),
    ]

    timestamp = models.DateTimeField(default=timezone.now, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    due_date = models.DateTimeField(blank=True, null=True)
    tags = models.ManyToManyField('Tag', blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='OPEN')
    def __str__(self):
            return self.title
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
            return self.name