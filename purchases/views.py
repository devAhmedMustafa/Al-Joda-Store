from django.shortcuts import render
from products.models import Product

# Create your views here.

def cart(request):


    return render(request, 'cart/cart.html',)

def add_to_cart(request, pk):
    
    product = 