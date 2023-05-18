from django.urls import path
from . import views

urlpatterns = [
    
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.orders, name='orders'),
    path('order/<int:order_id>/', views.order, name='order'),

]
