from django.db import models
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publishing_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True, upload_to="uploads/")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)