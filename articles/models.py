from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class ArticleManager(models.Manager):
    def get_active_articles(self) -> list:
        qs = Article.objects.filter(is_active=True)
        return qs


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, verbose_name='عنوان')
    slug = models.SlugField(unique=True, verbose_name='اسلاگ')
    image = models.ImageField(
        upload_to='articles/images/', verbose_name='تصویر')
    description = models.TextField(verbose_name='متن مقاله')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='تاریخ بروزرسانی')
    is_active = models.BooleanField(verbose_name='فعال/غیرفعال')

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        ordering = ['title', ]

    objects = ArticleManager()

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('articles:article_detail', args=[self.id, self.slug])
