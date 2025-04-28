from django.db import models

# Create your models here.


class Department(models.Model):
    department_name = models.CharField(max_length=200, null=True,blank=True)

    def __str__(self):
        return self. department_name
    
# models.py
class Doctors(models.Model):
    doctor_name = models.CharField(max_length=255, null=True, blank=True)
    department_name = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='doctors/', null=True, blank=True)

    def __str__(self):
        return self.doctor_name 

class Appoinment(models.Model):
    First_name = models.CharField(max_length=200, null=True, blank=True)
    Last_name = models.CharField(max_length=200, null=True, blank=True)
    Email = models.EmailField(max_length=254, null=True, blank=True)
    Phone = models.CharField(max_length=254, null=True, blank=True)
    Patient_name = models.CharField(max_length=254, null=True, blank=True)    
    doctor_name = models.ForeignKey(Doctors, on_delete=models.CASCADE, null=True, blank=True)
    department_name = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    Date = models.CharField(max_length=254, null=True, blank=True)
    Massage = models.TextField(max_length=254, null=True, blank=True)

class Contact(models.Model):
    name = models.CharField(max_length=200, null=True , blank=True)
    Email = models.EmailField(max_length=254, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True , blank=True)

