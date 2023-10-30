from django.contrib import admin
from django.urls import path

from post.views import *

urlpatterns = [
    path("post", post)
]