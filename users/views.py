from django.views.generic import CreateView
from users.forms import RegisterForm
from django.urls import reverse_lazy


class RegisterView(CreateView):
    template_name = "users/register.html"
    form_class = RegisterForm
    success_url = "/"