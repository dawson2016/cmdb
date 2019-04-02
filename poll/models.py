from django.db import models

# Create your models here.
class Polls(models.Model):
    pv= models.IntegerField(unique=True)
