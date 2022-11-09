from posts.models import *
from django import forms


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