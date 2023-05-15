from django.db import models
from users.models import CustomUser as User
from products.models import Product
from datetime import datetime, date
# Create your models here.


class CartItem(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_item')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_item')
    quantity = models.IntegerField(default=1)
    added_date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.user.username
    

class Cart(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')
    items = models.ManyToManyField(CartItem, blank=True)


class Orders(models.Model):

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='order')
    delivery_date = models.DateField(default=date.now())
