from django.shortcuts import render, redirect
from .models import Order, OrderItem
from django.http import HttpResponse, JsonResponse
from purchases.models import CartItem, Cart
from users.models import ShippingData
from django.db.models import Count
from django.contrib.auth.decorators import login_required


@login_required
def checkout(request):
    
    if request.method == 'POST':

        payment_method = request.POST.get('payment_method')
        address = request.POST.get('address')
        city = request.POST.get('city')
        phone_number = request.POST.get('phone_number')

        try:
            shipping_data = ShippingData.objects.get(user=request.user)

            shipping_data.phone_number = phone_number
            shipping_data.address = address
            shipping_data.city = city

            shipping_data.save()

        except ShippingData.DoesNotExist:

            shipping_data = ShippingData.objects.create(
                user = request.user,
                phone_number = phone_number,
                address = address,
                city = city,
            )

        if payment_method == 'cash':
            return redirect('create_order')
        
        elif payment_method == 'paypal':
            return redirect('payment_process')

    user = request.user
    cart = Cart.objects.get(user=user)
    cart_items = CartItem.objects.filter(cart=cart)

    context = {
        'cart_items': cart_items,
    }

    return render(request, 'delivere/checkout.html', context)


@login_required
def create_order(request):
 
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

    return redirect('orders')


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