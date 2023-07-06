from django.shortcuts import render, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView


class RegiserView(CreateView):
    template_name = 'users/register.html'
    form_class = UserCreationForm
    
    def get_success_url(self):
        return reverse('index')


class JustView(LoginView):
    template_name = 'users/register.html'
    
    def get_success_url(self):
        return reverse('index')
    
    