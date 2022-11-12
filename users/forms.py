from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from users.models import UserProfile


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    username = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta(UserCreationForm):
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")


class UserProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwarsg):
        super(UserProfileForm, self).__init__(*args, **kwarsg)

        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.field_class = "mt-10"
        self.helper = Layout(
            Field("birth_day", css_class="single-input"),
            Field("bio", css_class="single-input"),
            Field("image", css_class="single-input"),
        )

        self.helper.add_input(Submit("submit", "Update", css_class="primary-btn submit_btn"))

    class Meta:
        model = UserProfile
        fields = ("birth_day", "bio", "image")