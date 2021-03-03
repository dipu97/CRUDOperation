from django.db import models

# Create your models here.
class DataSet(models.Model):
    name=models.CharField(max_length=250)
    address=models.CharField(max_length=250)
    email=models.EmailField(max_length=35)
    education=models.CharField(max_length=250)
    def __str__(self):
        return self.name