from django.contrib import admin
from django.urls import path
from account.views import *

urlpatterns = [
    path("login", login1),
    path("home", home),
    path("register", register),
    path("registration", registration)
]