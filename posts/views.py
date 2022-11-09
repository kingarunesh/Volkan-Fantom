from django.views.generic import ListView, DetailView
from posts.models import Post, Category, Tag
from django.shortcuts import get_object_or_404


class IndexView(ListView):
    model = Post
    template_name = "posts/index.html"
    context_object_name = "posts"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
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