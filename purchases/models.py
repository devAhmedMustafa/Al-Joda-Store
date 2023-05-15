from django.db import models
from users.models import CustomUser as User
from products.models import Product
from datetime import datetime, date
# Create your models here.

class Cart(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')

    def __str__(self):
        return self.user.email


class CartItem(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_item')
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_item')


class Order(models.Model):

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='order')
    order_date = models.DateField(default=datetime.now())
