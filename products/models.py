from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    slug = models.SlugField(default="اسلاگ", allow_unicode=True, unique=True, verbose_name="اسلاگ")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def get_absolute_url(self):
        return reverse('products:product_category', args=[self.id])


class ProductManager(models.Manager):
    def get_active_products(self):
        qs = Product.objects.filter(is_active=True)
        if qs:
            return qs


class Product(models.Model):
    category = models.ManyToManyField(
        Category, related_name="category", verbose_name="دسته بندی")
    title = models.CharField(max_length=250, verbose_name='عنوان محصول')
    slug = models.SlugField(unique=True, allow_unicode=True, verbose_name='اسلاگ')
    price = models.IntegerField(default=0.00, verbose_name="قیمت")
    description = models.TextField(verbose_name='توضیحات محصول')
    main_image = models.ImageField(
        upload_to=f'products/images/', verbose_name='عکس اصلی')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='تاریخ بروزرسانی')
    is_active = models.BooleanField(verbose_name='فعال/غیرفعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
        ordering = ['title', ]

    def get_absolute_url(self):
        return reverse('products:product_detail', args=[self.slug])

    objects = ProductManager()


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to=f'products/images/', verbose_name='تصویر')

    class Meta:
        verbose_name = "گالری تصاویر"
        verbose_name_plural = "گالری تصاویر"
