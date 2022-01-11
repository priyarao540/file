from django.db import models

class studentsinfo(models.Model):
    name = models.CharField(null=True, max_length=100)
    address = models.TextField(null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(null=True, max_length=100)
    s_class=models.CharField(null=True,max_length=10)


# Create your models here.
