from django import views
from django.urls import path
from .views import ShowProfile, UserRegister, UserUpdate, PasswordsChangeView, EditProfile, CreateProfilePage 
from . import views


urlpatterns = [
   path('register/', UserRegister.as_view(), name='register'),
   path('updateProfile/', UserUpdate.as_view(), name='updateProfile'),
   path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
   path('password_success/', views.password_success, name='password_success'),
   path('<int:pk>/profile', ShowProfile.as_view(), name='showProfile'),
   path('<int:pk>/editProfile', EditProfile.as_view(), name='editProfile'),
   path('createProfilePage', CreateProfilePage.as_view(), name='createProfilePage'),
   

]