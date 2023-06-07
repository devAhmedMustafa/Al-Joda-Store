from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from users.models import ShippingData, CustomUser as User
from products.models import Product

class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False, null=True)
    ship_data = models.ForeignKey(ShippingData, on_delete=models.CASCADE, unique=False)
    date = models.DateField(default=timezone.now)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    status = models.CharField(max_length=30, default='pending', null=True)
    paid = models.BooleanField(default=False, null=True)
    


class OrderItem(models.Model):

    quantity = models.IntegerField(null=True, default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

