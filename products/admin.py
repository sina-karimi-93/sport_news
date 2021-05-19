from django.contrib import admin
from .models import Product, ProductImage, Category
# Register your models here.

admin.site.register(Category)


class ProductImageAdmin(admin.TabularInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_active', 'created',)
    list_display_links = ('id', 'title', )
    search_fields = ('title', 'description',)
    list_filter = ('is_active', 'created', 'updated',)
    list_editable = ('is_active',)
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ProductImageAdmin, ]
