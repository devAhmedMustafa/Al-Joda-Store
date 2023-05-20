from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from purchases.models import Cart, CartItem
from django.conf import settings
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from paypal.standard.forms import PayPalPaymentsForm
from .models import Payment

def payment_completed(request):

    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total = 0
    for item in cart_items:
        total += item.product.price * item.quantity

    total = total / 30

    payment = Payment.objects.create(
        user=request.user,
        amount=total,
        cart_order=cart
    )

    return redirect('create_order')

def payment_failed(request):
    

    return render(request, 'payment/payment_failed.html')



def payment_process(request):
    
    host = request.get_host()

    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total = 0
    for item in cart_items:
        total += item.product.price * item.quantity

    total = total / 30

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': str(total),
        'item_name': 'Item_Name_xyz',
        'invoice': 'Test Payment Invoice',
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format(host, reverse('payment_canceled')),
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'payment/payment_process.html', {'form': form})
