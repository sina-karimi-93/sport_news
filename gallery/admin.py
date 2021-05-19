from django.contrib import admin
from .models import Gallery,GalleryImage


class GalleryImageAdmin(admin.TabularInline):
    model = GalleryImage

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_active', 'created',)
    list_display_links = ('id', 'title', )
    search_fields = ('title',)
    list_filter = ('is_active', 'created', 'updated',)
    prepopulated_fields = {"slug": ("title",)}
    inlines = [GalleryImageAdmin, ]