from django.db import models
from datetime import datetime  

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
    loaned_date = models.DateTimeField(default=datetime.now, blank=True)
    returned = models.BooleanField(default=False)
    returned_date = models.DateTimeField(default='1800-01-01')
    