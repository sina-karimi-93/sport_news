from django.contrib import admin
from .models import Notification
# Register your models here.


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_active', 'created',)
    list_display_links = ('id', 'title', )
    search_fields = ('title', 'description',)
    list_filter = ('is_active', 'created', 'updated',)
    prepopulated_fields = {"slug": ("title",)}
