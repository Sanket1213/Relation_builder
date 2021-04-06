from django.db import models

# Create your models here.
class Relation(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
        
class User(models.Model):
    name1=models.CharField(max_length=100)
    name2=models.CharField(max_length=100)
    relation=models.CharField(max_length=100, default='')