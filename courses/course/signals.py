from django.db.models.signals import post_save, pre_delete
from authentication.models import User
from django.dispatch import receiver
from .models import Cart
 
 
from django.db.models.signals import post_save
#signals_section
def create_profile(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(userCart=instance)



post_save.connect(create_profile, sender=User)
