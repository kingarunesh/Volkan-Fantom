from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from posts.models import Post, Category, Tag
from django.shortcuts import get_object_or_404
from posts.forms import PostCreationForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify



class IndexView(ListView):
    model = Post
    template_name = "posts/index.html"
    context_object_name = "posts"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["slider_posts"] = Post.objects.filter(slider_post=True).order_by("-id").all()
        return context


class PostDetail(DetailView):
    model = Post
    template_name = "posts/detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        return context


class CategoryDetail(ListView):
    model = Post
    template_name = "categories/category-detail.html"
    context_object_name = "posts"

    def get_queryset(self):
        self.category = get_object_or_404(Category, pk=self.kwargs["pk"])
        return Post.objects.filter(category=self.category).order_by("-id")

    def get_context_data(self,**kwargs):
        context = super(CategoryDetail, self).get_context_data(**kwargs)
        self.category = get_object_or_404(Category, pk=self.kwargs["pk"])
        context["category"] = self.category
        return context


class TagDetail(ListView):
    model = Post
    template_name = "tags/tag-detail.html"
    context_object_name = "posts"

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, slug=self.kwargs["slug"])
        return Post.objects.filter(tag=self.tag).order_by("-id")
    
    def get_context_data(self, **kwargs):
        context = super(TagDetail, self).get_context_data(**kwargs)
        self.tag = get_object_or_404(Tag, slug=self.kwargs["slug"])
        context["tag"] = self.tag
        return context


# @method_decorator(login_required(login_url="users/login"), name="dispatch")
class CreatePostView(LoginRequiredMixin, CreateView):
    template_name = "posts/create-post.html"
    model = Post
    form_class = PostCreationForm

    def get_success_url(self):
        return reverse_lazy("detail", kwargs={"pk": self.object.pk, "slug": self.object.slug})

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()

        tags = self.request.POST.get("tag").split(",")

        for tag in tags:
            current_tag = Tag.objects.filter(slug=slugify(tag))
            if current_tag.count() < 1:
                create_tag = Tag.objects.create(title=tag)
                form.instance.tag.add(create_tag)
            else:
                existed_tag = Tag.objects.get(slug=slugify(tag))
                form.instance.tag.add(existed_tag)
        
        return super(CreatePostView, self).form_valid(form)