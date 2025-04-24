from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import CustomLoginForm

# Create your views here.
class CustomLoginView(LoginView):
    template_name = "login.html"
    authentication_form = CustomLoginForm


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("login")

