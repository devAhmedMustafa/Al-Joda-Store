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

def cart(request):

    categories = Category.objects.all()

    return render(request, 'cart/cart.html', {'categories': categories})

def categored_products(request, pk):

    categories = Category.objects.all()
    category = Category.objects.get(pk=pk)
    products = Product.objects.filter(category=category)

    return render(request, 'products/page-product.html', {'categories': categories,'category': category, 'products': products})

def search(request):

    search_filter = request.GET.get('search')

    products = Product.objects.filter(name__icontains=search_filter)

    data = {
        
    }

    return JsonResponse(data)
