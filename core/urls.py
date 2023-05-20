from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('products.urls')),
    path('', include('purchases.urls')),
    path('', include('orders.urls')),
    path('', include('payments.urls')),
    path('paypal/', include('paypal.standard.ipn.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
