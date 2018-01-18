from django.db import models

class Cadet(models.Model):
    first = models.CharField(max_length=200)
    last = models.CharField(max_length=200)
    xnumber = models.CharField(max_length=8)

# Create your models here.
