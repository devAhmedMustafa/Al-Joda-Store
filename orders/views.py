from django.shortcuts import render
from .models import Order, OrderItem
from django.http import JsonResponse
from purchases.models import CartItem, Cart
from users.models import ShippingData
from django.db.models import Count
from django.contrib.auth.decorators import login_required


@login_required
def checkout(request):
 
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)

    if cart_items.exists():

        order = Order.objects.create(
        user = request.user,
        ship_data = ShippingData.objects.get(user=request.user)
        )

        for cart_item in cart_items:
            OrderItem.objects.create(
                product = cart_item.product,
                order = order,
            )

        cart.delete()

    data = {
        'message': 'done',
    }

    return JsonResponse(data)


def orders(request):

    user = request.user
    carts = Cart

    return render(request, 'delivere/orders.html')