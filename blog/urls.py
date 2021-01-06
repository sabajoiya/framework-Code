from django.urls import path, include
from . import views
from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()
router.register(r'post', views.post_view)


urlpatterns = [
    path('', include(router.urls)),
]
