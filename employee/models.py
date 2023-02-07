from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.

class Department(models.Model):
    name = models.TextField()
    description = models.TextField()
    status = models.IntegerField()
    create_date = models.DateTimeField(default=timezone.now) 
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

