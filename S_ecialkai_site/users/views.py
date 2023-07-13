from django.shortcuts import render, reverse, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib.auth import login, logout


class RegiserView(CreateView):
    template_name = 'users/register.html'
    form_class = UserCreationForm
    
    # def get_success_url(self):
    #     return reverse('index')
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')
    
class JustView(LoginView):
    template_name = 'users/login.html'
    form_class = AuthenticationForm
    
    def get_success_url(self):
        return reverse('index')
    
def exit(request):
    logout(request)
    return redirect('index')