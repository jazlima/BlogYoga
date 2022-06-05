from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from .forms import SignUpForm, UpdateForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic import DetailView
from AppBlogYoga.models import Profile

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

class ShowProfile(DetailView):
    model = Profile
    template_name = 'registration/showProfile.html'

    def get_context_data(self, *args, **kwargs):
        contexto=super(ShowProfile, self).get_context_data(*args, **kwargs)
        page_user=get_object_or_404(Profile, id=self.kwargs['pk'])
        contexto['page_user']=page_user
        return contexto 

