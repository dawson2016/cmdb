from django.db import models

# Create your models here.

class Hostlist(models.Model):
    name = models.CharField(max_length=30)
    wanip = models.CharField(max_length=30)
    lanip = models.CharField(max_length=30)
    status = models.CharField(max_length=10)
    cpu = models.CharField(max_length=10)
    mem = models.CharField(max_length=10)
    disk = models.CharField(max_length=10)
    ostype = models.CharField(max_length=10)
    usedate = models.CharField(max_length=20)
    usage = models.CharField(max_length=50)
    instanceid = models.CharField(max_length=50)
    def __str__(self):
        return self.lanip        
