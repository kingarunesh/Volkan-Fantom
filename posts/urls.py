from django.urls import path
from posts.views import *


urlpatterns = [
    path("", IndexView.as_view(), name="index")
]