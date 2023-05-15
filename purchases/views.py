from django.shortcuts import render
from products.models import Product
from .models import Cart, CartItem
from django.http import JsonResponse

# Create your views here.

def cart(request):

    user = request.user
    cart = Cart.objects.get(user=user)
    cart_items = CartItem.objects.filter(cart=cart)

    context = {
        'cart_items': cart_items
    }

    return render(request, 'cart/cart.html',)


def add_to_cart(request):

    pk = request.GET.get('pk')
    quantity = request.GET.get('quantity')

    user = request.user
    product = Product.objects.get(pk=pk)
    cart_item = CartItem.objects.create(

        product = product,
        quantity = quantity,

    )

    try:

        cart = Cart.objects.get(user=user)

    except:
        cart = Cart.objects.create()

    cart_item.cart = cart

    cart_item.save()

    data = {
        'message': 'success',
    }

    return JsonResponse(data)
