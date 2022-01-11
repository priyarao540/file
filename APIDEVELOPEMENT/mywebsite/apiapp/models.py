from django.db import models

class photography (models.Model):
    Camera_name=models.CharField(max_length=100, null=True)
    Camera_price=models.IntegerField( null=True)



# Create your models here.
