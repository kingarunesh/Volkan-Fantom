from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
import readtime 


class Category(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.title
    
    def post_count(self):
        return self.posts.all().count()


class Tag(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    def post_count(self):
        return self.posts.all().count()


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publishing_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True, upload_to="uploads/")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(default="slug", editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, related_name="posts")
    tag = models.ManyToManyField(Tag, related_name="posts", blank=True)
    slider_post = models.BooleanField(default=False)
    hit = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
    
    def get_readtime(self):
      result = readtime.of_text(self.content)
      return result.text
        
    def __str__(self):
        return self.title
    
    def post_tag(self):
        return ','.join(str(tag) for tag in self.tag.all())
    
    class Meta:
        ordering = ['-id']