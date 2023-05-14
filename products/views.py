from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Product, Category
import json
# Create your views here.


def home(request):
    
    categories = Category.objects.all()
    products = Product.objects.all()

    print(categories)
    print(products)

    return render(request, 'home.html', {'products': products, 'categories': categories})


def products(request):

    categories = Category.objects.all()
    products = Product.objects.all()

    print(categories)
    print(products)

    return render(request, 'products/products.html', {'products': products, 'categories': categories})



def search(request):

    search_filter = request.GET.get('search')

    products = Product.objects.filter(name__icontains=search_filter)

    data = {
        
    }

    return JsonResponse(data)
