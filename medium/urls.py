from django.contrib import admin
from django.urls import path, include
from apps.reviews.views import ProductViewSet
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='Product')

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
