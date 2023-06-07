from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from .forms import NewUser
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.http import HttpResponse, JsonResponse
from .functions import send_email_verify
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, authentication, status
from .serializers import UserSerializer
from .models import CustomUser as User, ShippingData
from .token import account_activation_token
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from products.models import Category

def activate(request, pk, token):

    try:
        user = User.objects.get(pk=pk)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        auth_login(request, user)

    return HttpResponse('account activated')


class UserList(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permissions_classes = [permissions.IsAuthenticated]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


def email_sent(request):

    return render(request, 'authentication/email_sent.html')


# NORMAL DJANGO
def sign_up(request):
    if request.method == 'POST':
        domain = get_current_site(request).domain

        form = NewUser(request.POST)
        if form.is_valid():

            user = form.save(commit=False)
            user.is_active = False
            user.save()
            
            send_email_verify(user, domain)
            
            return redirect('/email_sent')

    form = NewUser()

    return render(request, 'authentication/authentication.html', {'form': form, 'title': 'Sign Up'})


def login(request):

    form = AuthenticationForm()

    if request.method == 'POST':

        form = AuthenticationForm(request, data=request.POST)
        domain = get_current_site(request).domain

        if form.is_valid():

            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = User.objects.get(email__exact=email)

            if user.is_active:

                user = authenticate(email=email, password=password)
                if user is not None:
                    auth_login(request, user)
                    return redirect('home')

                else:
                    return render(request,'authentication/authentication.html',{'form': form, 'error': 'Invalid email or password'})

            else:
                send_email_verify(user, domain)
                return redirect('email_sent')

    return render(request, 'authentication/authentication.html', {'form': form, 'title': 'Login'})

@login_required
def logout(request):
    auth_logout(request)
    return JsonResponse({'message': 'logged out'})


@login_required
def profile(request, email):

    context = {
        'user': request.user,
        'categories': Category.objects.all(),
        'ship_data': ShippingData.objects.get(user=request.user),
    }

    return render(request, 'authentication/profile.html', context)

def user_validation(request):

    email = request.GET.get('email')
    is_taken = User.objects.filter(email__iexact=email).exists()

    data = {'is_taken': is_taken}

    return JsonResponse(data)