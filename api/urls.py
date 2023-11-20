from django.urls import path, include
from api.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'post', PostViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]
