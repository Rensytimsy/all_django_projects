from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from decouple import config

router = DefaultRouter()
api_prefix = config("API_PREFIX")

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f"{api_prefix}", include("store.urls"))
]
