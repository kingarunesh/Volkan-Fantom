from posts.models import *
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Field, Layout


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
        self.helper.layout = Layout(
            Field("title", css_class="single-input", placeholder="Post Title"),
            Field("content", css_class="single-input", placeholder="Post Content"),
            Field("category", css_class="single-input"),
            Field("tag", css_class="single-input", placeholder="Tags", value=self.instance.post_tag()),
            Field("image", css_class="single-input")
        )
        self.helper.add_input(Submit("submit", "Update", css_class="genric-btn success-border circle"))

    tag = forms.CharField()

    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "image",
            "category",
        ]


class CreateCommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateCommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Field("name", css_class="form-control"),
            Field("email", css_class="form-control"),
            Field("content", css_class="form-control mb-10"),
        )

        self.helper.add_input(Submit("submit", "Post Comment", css_class="primary-btn submit_btn"))
    
    class Meta:
        model = Comment
        fields = [
            "name",
            "email",
            "content"
        ]
