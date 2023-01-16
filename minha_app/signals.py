from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Loan

@receiver(post_save, sender=Loan)
def create_loan(sender, instance, **kwargs):
    qnt_loans = Loan.objects.filter(material=instance.material, returned=False).count()
    instance.material.qnt_available = instance.material.qnt - qnt_loans
    instance.material.save()
        
@receiver(post_delete, sender=Loan)
def delete_loan(sender, instance, **kwargs):
    print('deletando...')
    qnt_loans = Loan.objects.filter(material=instance.material, returned=False).count()
    instance.material.qnt_available = instance.material.qnt - qnt_loans
    instance.material.save()
        
