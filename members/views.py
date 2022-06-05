from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import SignUpForm, UpdateForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm

class UserRegister(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserUpdate(generic.UpdateView):
    form_class = UpdateForm
    template_name = 'registration/updateProfile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')
    template_name = 'registration/change-password.html'

def password_success(request):
    return render(request, 'registration/password_success.html', {})

