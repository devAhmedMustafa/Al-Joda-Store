from django.db import models
from users.models import CustomUser as User
from products.models import Product
from django.utils import timezone


class Cart(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


class CartItem(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)

    class Meta:

        unique_together = ['product', 'cart']
