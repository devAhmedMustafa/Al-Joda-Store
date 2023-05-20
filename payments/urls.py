from django.urls import path
from . import views

urlpatterns = [

    path('payment-process/', views.payment_process, name='payment_process'),
    path('payment-completed/', views.payment_completed, name='payment_done'),
    path('payment-failed/', views.payment_failed, name='payment_canceled'),

]