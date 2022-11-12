from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from users.forms import RegisterForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from users.models import UserProfile
from users.forms import UserProfileForm


class RegisterView(CreateView):
    template_name = "users/register.html"
    form_class = RegisterForm
    success_url = "/"


class UserLoginView(LoginView):
    template_name = "users/login.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect("/")
        return super(UserLoginView, self).dispatch(request, *args, **kwargs)


class UserLogoutView(LogoutView):
    template_name = "users/login.html"


class UserUpdateProfileView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    template_name = "users/profile-update.html"
    form_class = UserProfileForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(UserUpdateProfileView, self).form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("users:update_profile", kwargs={"slug": self.object.slug})
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user != request.user:
            return HttpResponseRedirect("/")
        
        return super(UserUpdateProfileView, self).get(request, *args, **kwargs)