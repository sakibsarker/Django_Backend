from django.db import models

class Feature(models.Model):
    names=models.CharField(max_length=100)
    details=models.CharField(max_length=500)