from django.db import models

# Create your models here.
class Swim (models.Model):
    name = models.TextField(max_length = 100)
    age = models.IntegerField(default=0)
    club = models.TextField(max_length = 200)
    fr = models.FloatField() 
    bu = models.FloatField()
    ba = models.FloatField()
    br = models.FloatField()
    img = models.TextField(max_length=8192, null=True)
