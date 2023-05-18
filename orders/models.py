from django.db import models
from django.utils import timezone
from users.models import ShippingData, CustomUser as User
from products.models import Product

class Order(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False, null=True)
    ship_data = models.ForeignKey(ShippingData, on_delete=models.CASCADE, unique=False)
    date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=30, default='pending')
    paid = models.BooleanField(default=False)


class OrderItem(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

