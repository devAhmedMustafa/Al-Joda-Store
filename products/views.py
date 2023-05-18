from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Product, Category
import json


def home(request):
    
    user = request.user
    categories = Category.objects.all()
    products = Product.objects.all()

    context = {
        'products': products,
        'categories': categories,
    }

    return render(request, 'home.html', context)


def products(request):

    user = request.user
    categories = Category.objects.all()
    products = Product.objects.all()

    context = {
        'products': products,
        'categories': categories
    }

    return render(request, 'products/products.html', context)


def categored_products(request, slug):

    categories = Category.objects.all()
    category = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=category)

    context = {
        'categories': categories,
        'category': category,
        'products': products,
        'title': category.name,
    }

    return render(request, 'products/page-product.html', context)


def search(request):

    search_filter = request.GET.get('search_value')

    categories = Category.objects.all()
    products = Product.objects.filter(name__icontains=search_filter)

    context = {
        'categories': categories,
        'products': products,
        'title': 'نتائج البحث',
    }

    return render(request, 'products/page-product.html', context)

def searchAJAX(request):

    search_filter = request.GET.get('search_value')

    products = Product.objects.filter(name__icontains=search_filter).values()

    data = {
        'products': json.dumps(list(products))
    }

    return JsonResponse(data)

def product(request, slug):

    product = Product.objects.get(slug=slug)

    context = {
        'product': product,
        'categories': Category.objects.all(),
    }

    return render(request, 'products/one-product.html', context)