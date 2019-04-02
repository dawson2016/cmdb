from django.db import models

# Create your models here.
class Audit(models.Model):
    proname = models.CharField(max_length=30)
    proenv = models.CharField(max_length=30)
    status = models.IntegerField(default=0)
    comment = models.CharField(max_length=30)
    def __str__(self):
        return self.proname
