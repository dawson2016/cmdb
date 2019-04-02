from django.db import models
from index.models import Hostlist
# Create your models here.
class Portlist(models.Model):
    ipaddr = models.ForeignKey(Hostlist)
    lanport = models.CharField(max_length=6)
    wanport = models.IntegerField(unique=True)
    status = models.IntegerField(2)
    comment = models.CharField(max_length=30)
    def __str__(self):
        return self.ipaddr
