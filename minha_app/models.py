from django.db import models

# Create your models here.
class Material(models.Model):
    name = models.CharField(max_length=300)
    qnt = models.IntegerField()
    def __str__(self):
        return self.name

class Loan(models.Model):
    beneficiary = models.CharField(max_length=300)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    responsible = models.CharField(max_length=300)    
    