from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    
    user = request.user
    
    return HttpResponse(f'Hello{user.first_name}')
