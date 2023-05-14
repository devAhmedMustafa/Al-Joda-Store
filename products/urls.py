from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/', views.products),
    path('cart/', views.cart, name='cart'),
    path('categried/<int:pk>/', views.categored_products, name="categoried")
]