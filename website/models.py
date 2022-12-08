from django.db import models
from course.models import Cart

# Create your models here.
class mony(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.PROTECT)
    price = models.FloatField()
    date = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self) -> str:
        return self.cart.userCart.username