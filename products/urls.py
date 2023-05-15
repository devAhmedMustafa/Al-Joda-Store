from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/', views.products),
    path('categried/<int:pk>/', views.categored_products, name="categoried"),
    path('search/', views.search, name="search")
]