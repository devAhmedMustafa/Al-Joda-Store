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



def categored_products(request, pk):

    categories = Category.objects.all()
    category = Category.objects.get(pk=pk)
    products = Product.objects.filter(category=category)

    context = {
        'categories': categories,
        'category': category,
        'products': products
    }

    return render(request, 'products/page-product.html', context)

def search(request):

    search_filter = request.GET.get('search_value')

    products = Product.objects.filter(name__icontains=search_filter).values()

    data = {
        'products': json.dumps(list(products))
    }

    return JsonResponse(data)
