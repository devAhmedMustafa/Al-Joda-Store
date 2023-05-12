from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Product
import json
# Create your views here.


def home(request):
    
    user = request.user

    return HttpResponse(f'Hello{user.first_name}')


def products(request):

    products = Product.objects.all()

    return render(request, 'products/products.html', {'products': products}) # type: ignore



def search(request):

    search_filter = request.GET.get('search')

    products = Product.objects.filter(name__icontains=search_filter)

    data = {
        
    }

    return JsonResponse(data)
