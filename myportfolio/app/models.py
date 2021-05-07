from django.db import models

# Create your models here.
class contact(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Subject = models.CharField(max_length=100)
    Message = models.CharField(max_length=100)
