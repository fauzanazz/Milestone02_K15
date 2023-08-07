from django.db import models
from django.contrib.auth.models import User
from makanan.models import MenuItem
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    total_price = models.IntegerField(default=0)

class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    total_items = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return str(self.user.username) + " " + str(self.items.name)
    
@receiver(post_save, sender=CartItems)
def _post_save_receiver(sender, **kwargs):
    cart_items = kwargs['instance']
    price_total = MenuItem.objects.get(id=cart_items.items.id)
    cart_items.price = cart_items.quantity * int(price_total.price)
    total_cart_items = CartItems.objects.filter(user = cart_items.user )
    cart = Cart.objects.get(id = cart_items.cart.id)
    cart.total_price = cart_items.price
    cart.save()

