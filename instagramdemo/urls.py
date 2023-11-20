from django.contrib import admin
from django.urls import path, include
from instagramdemo import settings
from post import url as postUrl
from chat import url as chatUrl
from account import url as accountUrl
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(postUrl)),
    path('', include(chatUrl)),
    path('', include(accountUrl)),
    path('api/', include('api.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
