from django.contrib import admin
from django.urls import path , include
from post import url as postUrl
from chat import url as chatUrl
from account import url as accountUrl

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(postUrl)),
    path('', include(chatUrl)),
    path('', include(accountUrl)),
]
