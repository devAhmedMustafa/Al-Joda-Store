from django.shortcuts import render
from products.models import Product
from .models import Cart, CartItem
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required



@login_required
def cart(request):

    user = request.user
    try:
        cart = Cart.objects.get(user=user)

    except:
        cart = Cart.objects.create(user=user)

    cart_items = CartItem.objects.filter(cart=cart)

    context = {
        'cart_items': cart_items
    }

    return render(request, 'cart/cart.html', context)


def add_to_cart(request):

    pk = request.GET.get('pk')
    quantity = request.GET.get('quantity')

    user = request.user
    product = Product.objects.get(pk=pk)

    try:

        cart = Cart.objects.get(user=user)

    except:
        cart = Cart.objects.create(user=user)

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()

    except:

        cart_item = CartItem.objects.create(

            product = product,
            quantity = quantity,
            cart = cart

        )

    data = {
        'message': 'success',
    }

    return JsonResponse(data)
