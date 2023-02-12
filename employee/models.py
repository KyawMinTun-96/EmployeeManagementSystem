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



class Position(models.Model):
    name = models.TextField()
    description = models.TextField()
    status = models.IntegerField()
    create_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    code  = models.CharField(max_length=100, blank=True)
    firstname  = models.TextField()
    middlename  = models.TextField(blank=True, null=True)
    lastname = models.TextField()
    gender  = models.TextField(blank=True, null=True)
    dob  = models.DateField(blank=True, null=True)
    contact  = models.TextField()
    address  = models.TextField()
    email  = models.TextField()
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    position_id = models.ForeignKey(Position, on_delete=models.CASCADE) 
    hired_date = models.DateTimeField()
    salary  = models.FloatField(default=0)
    status = models.IntegerField()
    create_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstname + ' ' + self.middlename + ' ' + self.lastname + ' ' + self.position_id.id + ' ' + self.department_id.id



class Project(models.Model):

    name = models.CharField(max_length=100, blank=True)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.IntegerField()
    create_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ' ' + self.department_id.id + ' '

