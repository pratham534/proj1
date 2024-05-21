from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.CharField(max_length=20, unique=True)
    city = models.CharField(max_length=50)
    marks = models.IntegerField()
    company = models.ForeignKey('Company', on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Company(models.Model):
    name = models.CharField(max_length=50, unique=True)
    number_of_emp = models.IntegerField()
    logo = models.ImageField(upload_to='images/logo/', null=True, blank=True)

    def __str__(self):
        return self.name