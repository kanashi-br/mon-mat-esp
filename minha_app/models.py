from django.db import models

# Create your models here.
class Material(models.Model):
    name = models.CharField(max_length=300)
    qnt = models.IntegerField()