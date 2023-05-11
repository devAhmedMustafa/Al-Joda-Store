from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
import json
# Create your views here.


def home(request):
    
    user = request.user
    

    return HttpResponse(f'Hello{user.first_name}')

def products(request):

    products = Product.objects.get(name = 'IPhone 6')

    details = products.details

    return render(request, 'products/products.html', {'products': products, 'details': details.items})
