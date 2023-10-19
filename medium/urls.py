from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from apps.reviews.views import ProductViewSet

router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='Product')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("/", include(router.urls)),
    
]
