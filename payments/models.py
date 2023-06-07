from django.db import models
from users.models import CustomUser as User
from purchases.models import Cart

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    cart_order = models.ForeignKey(Cart, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} - {self.amount}'
