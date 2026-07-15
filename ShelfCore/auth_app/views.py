from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView 
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy 

from .forms import SignupForm
# Create your views here.

class SigninView(LoginView):
    template_name = 'signin/signin.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')
    
class SignoutView(LogoutView):
    next_page = 'signin'
    
class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'signup/signup.html'
    success_url = reverse_lazy('signin')