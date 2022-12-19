from django.db.models.signals import post_save, pre_delete
from authentication.models import User
from django.dispatch import receiver
from .models import Cart
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from authentication.views import RegisterView
 
from django.db.models.signals import post_save
#signals_section
def create_profile(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(userCart=instance)



post_save.connect(create_profile, sender=User)


def update_cart(sender,instance,created,**kwargs):
    if created:
        p = Cart.objects.get(userCart = instance)
        current_site = "https://onze-egypt.azurewebsites.net/pages/Puy/"
        
        print (p.pk)
        p.url = current_site + str(p.pk) + '/'
        p.save()
post_save.connect(update_cart , sender=User)