from django.db import models

# Create your models here.
class UserGroup(models.Model):
    name = models.CharField(max_length=80, unique=True)
    comment = models.CharField(max_length=40)
    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=80)
    group = models.ManyToManyField(UserGroup)
    perm = models.CharField(max_length=4)
    comment = models.CharField(max_length=30)
    def __str__(self):
        return self.name

            
class User(models.Model):
    name = models.CharField(max_length=80)
    role = models.CharField(max_length=10)
    group = models.ManyToManyField(UserGroup)
    def __str__(self):
        return self.name
