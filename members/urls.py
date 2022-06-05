from django import views
from django.urls import path
from .views import UserRegister, UserUpdate, PasswordsChangeView
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
   path('register/', UserRegister.as_view(), name='register'),
   path('updateProfile/', UserUpdate.as_view(), name='updateProfile'),
   path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
   path('password_success/', views.password_success, name='password_success'),
   

]