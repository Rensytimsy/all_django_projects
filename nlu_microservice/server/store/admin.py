from django.contrib import admin
from .models import Product, Store
from django.contrib.admin import ModelAdmin
# Register your models here.

@admin.register(Product)
class AdminProduct(ModelAdmin):
    list_display = ["id", "title", "price", "available", "get_product_store"]
    list_filter = ["available"]
    
@admin.register(Store)
class AdminStore(ModelAdmin):
    list_display = ["id", "name", "store_type", "description"]

