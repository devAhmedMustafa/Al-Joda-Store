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


@login_required
def orders(request):

    user = request.user
    orders = Order.objects.filter(user=user).annotate(Count('orderitem'))

    return render(request, 'delivere/orders.html')


@login_required
def order(request, order_id):
    
    user = request.user
    order = Order.objects.get(user=user, id=order_id)
    order_items = OrderItem.objects.filter(order=order)

    context = {
        'order': order,
        'order_items': order_items,
    }

    return render(request, 'delivere/order.html', context)