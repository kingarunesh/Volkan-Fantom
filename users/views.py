from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from users.forms import RegisterForm
from django.urls import reverse_lazy


class RegisterView(CreateView):
    template_name = "users/register.html"
    form_class = RegisterForm
    success_url = "/"


class UserLoginView(LoginView):
    template_name = "users/login.html"


class UserLogoutView(LogoutView):
    template_name = "users/login.html"