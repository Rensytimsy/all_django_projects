from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views, serializers

router = DefaultRouter()
router.register(r"products", views.ProductListView, basename="products")

urlpatterns = [
    path("", include(router.urls))
]
