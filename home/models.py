from django.db import models
from django.urls import reverse


class NewsManager(models.Manager):
    def get_active_news(self) -> list:
        qs = News.objects.filter(is_active=True)
        return qs


class News(models.Model):
    title = models.CharField(max_length=250, verbose_name='عنوان')
    slug = models.SlugField(unique=True, allow_unicode=True, verbose_name='اسلاگ')
    image = models.ImageField(
        upload_to='news/images/', verbose_name='تصویر')
    description = models.TextField(verbose_name='متن خبر')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='تاریخ بروزرسانی')
    is_active = models.BooleanField(verbose_name='فعال/غیرفعال')
    source_link = models.URLField(blank=True, null=True, verbose_name='منبع')

    class Meta:
        verbose_name = "خبر"
        verbose_name_plural = "اخبار"
        ordering = ['title', ]

    objects = NewsManager()

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('news:news_detail', args=[self.slug])
