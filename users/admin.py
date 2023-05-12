from django.contrib import admin
from .models import CustomUser as User, ShippingData
# Register your models here.

admin.site.register(User)
admin.site.register(ShippingData)
