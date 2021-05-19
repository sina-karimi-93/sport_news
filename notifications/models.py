from django.db import models
from django.urls import reverse


class NotificationManager(models.Manager):
    def get_active_notifications(self) -> list:
        qs = Notification.objects.filter(is_active=True)
        return qs


class Notification(models.Model):
    title = models.CharField(max_length=250, verbose_name='عنوان')
    slug = models.SlugField(unique=True, verbose_name='اسلاگ')

    description = models.TextField(verbose_name='متن اعلان')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='تاریخ بروزرسانی')
    is_active = models.BooleanField(verbose_name='فعال/غیرفعال')

    class Meta:
        verbose_name = "اعلان"
        verbose_name_plural = "اعلانات"
        ordering = ['title', ]

    objects = NotificationManager()

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('notifications:notification_detail', args=[self.id, self.slug])
