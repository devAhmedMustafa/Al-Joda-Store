from django.shortcuts import render
from products.models import Product
from .models import Cart, CartItem
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from products.models import Category


@login_required
def cart(request):

    user = request.user
    try:
        cart = Cart.objects.get(user=user)

    except:
        cart = Cart.objects.create(user=user)

    cart_items = CartItem.objects.filter(cart=cart)
    total = 0

    for i in cart_items:
        total += i.product.price * i.quantity

    context = {
        'categories': Category.objects.all(),
        'cart_items': cart_items,
        'total': total,
    }

    return render(request, 'cart/cartpage.html', context)


def add_to_cart(request):

    pk = request.GET.get('pk')
    quantity = int(request.GET.get('quantity'))

    user = request.user
    product = Product.objects.get(pk=pk)

    try:

        cart = Cart.objects.get(user=user)

    except:
        cart = Cart.objects.create(user=user)

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += quantity
        cart_item.save()

    except:

        cart_item = CartItem.objects.create(

            product=product,
            quantity=quantity,
            cart=cart

        )

    data = {
        'message': 'success',
    }

    return JsonResponse(data)


def change_quantity(request):

    new_quantity = request.GET.get('quantity')
    pk = request.GET.get('pk')

    cart_item = CartItem.objects.get(pk=pk)
    cart_item.quantity = new_quantity
    cart_item.save()

    data = {
        'message': 'success'
    }

    return JsonResponse(data)
