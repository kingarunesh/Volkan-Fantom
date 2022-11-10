from posts.models import *
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Field


class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post

        widgets = {
            "title": forms.TextInput(attrs={"class": "single-input", "placeholder": "Enter Post Title"}),
            "content": forms.Textarea(attrs={"class": "single-input", "placeholder": "Enter Post Content..."})
        }

        fields = [
            "title",
            "content",
            "image",
            "category",
        ]


class PostUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.field_class = "mt-10"
        self.helper.layout = (
            Field("title", css_class="single-input", placeholder="Post Title"),
            Field("content", css_class="single-input", placeholder="Post Content"),
            Field("Tag", css_class="single-input", placeholder="Tags"),
            Field("category", css_class="single-input"),
            Field("image", css_class="single-input")
        )
        self.helper.add_input(Submit("submit", "Update", css_class="genric-btn success-border circle"))

    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "image",
            "category",
        ]