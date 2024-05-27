from django.contrib import admin
from .models import Product, Category, Manufacturer
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'friendly_name')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'manufacturer', 'price', 'rating')
    search_fields = ('name', 'category__name', 'manufacturer__name')
    list_filter = ('category', 'manufacturer', 'rating')

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'website')