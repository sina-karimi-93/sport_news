from django.contrib import admin
from .models import Article
# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'is_active', 'created',)
    list_display_links = ('id', 'title', )
    search_fields = ('title', 'description',)
    list_filter = ('is_active', 'created', 'updated',)
    prepopulated_fields = {"slug": ("title",)}
