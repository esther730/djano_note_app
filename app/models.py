"""
Definition of models.
"""

from django.db import models
from datetime import datetime

PRIORITY_CHOICE = [
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High')
]

class Note(models.Model): 
    subject = models.CharField(max_length=500) 
    detail = models.TextField(null = True, blank=True)
    priority = models.TextField(max_length=6, choices=PRIORITY_CHOICE, default='medium')
    created_date = models.DateTimeField()
    last_modified = models.DateTimeField()
    is_deleted = models.BooleanField()

    def create(self):
        self.created_date = datetime.now()
        self.last_modified = datetime.now()
        self.is_deleted = False
        self.save()

    def edit(self):
        self.last_modified = datetime.now()
        self.save()

    def delete(self):
        self.last_modified = datetime.now()
        self.is_deleted = True
        self.save()
