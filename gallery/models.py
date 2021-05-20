from django.db import models
from django.urls import reverse
from django.utils.translation import activate
# Create your models here.


class GalleryManager(models.Manager):
    def get_active_galleries(self):
        qs = Gallery.objects.filter(is_active=True)
        if qs:
            return qs


class Gallery(models.Model):
    title = models.CharField(max_length=250, verbose_name="عنوان")
    slug = models.SlugField(unique=True,allow_unicode=True, verbose_name="اسلاگ")
    description = models.TextField(null=True, blank=True, verbose_name="توضیحات")
    image = models.ImageField(upload_to="gallery/", verbose_name="تصویر اصلی")
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="تاریخ بروزرسانی")
    is_active = models.BooleanField(default=True, verbose_name="فعال/غیرفعال")

    class Meta:
        verbose_name = "گالری"
        verbose_name_plural = "گالری"

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("gallery:gallery_detail", args=[self.slug])

    objects = GalleryManager()


class GalleryImage(models.Model):
    gallery = models.ForeignKey(
        Gallery,on_delete=models.CASCADE, verbose_name="گالری", related_name="gallery_image")
    image = models.ImageField(upload_to="gallery/", verbose_name="تصویر")
