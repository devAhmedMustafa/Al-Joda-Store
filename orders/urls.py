from django.urls import path
from . import views

urlpatterns = [
    
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.orders, name='orders'),
    path('orders/<int:order_id>/', views.order, name='order'),
    path('create_order/', views.create_order, name='create_order'),
]
