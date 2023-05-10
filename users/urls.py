from django.urls import path
from . import views


urlpatterns = [
    path('api/users/', views.UserList.as_view()),
    path('signup/', views.sign_up, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('activate/<pk>/<token>/', views.activate, name='activate'),
    path('email_sent/', views.email_sent, name='email_sent')
]
