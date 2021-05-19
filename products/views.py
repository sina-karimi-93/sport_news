from django.shortcuts import render, get_object_or_404
from .models import Product, Category, ProductImage


# Create your views here.


def product_list(request):
    products = Product.objects.get_active_products()
    categories = Category.objects.all()
    context = {
        "products": products,
        "categories": categories
    }

    return render(request, 'products_list.html', context)


def product_detail(request, pk, slug):
    product = get_object_or_404(Product, id=pk, slug=slug)
    product_gallery = ProductImage.objects.filter(product=product)
    products = Product.objects.get_active_products()
    context = {
        'product': product,
        "product_gallery": product_gallery,
        "products": products,
    }

    return render(request, 'products_detail.html', context)


def product_category(request, slug):
    category = Category.objects.filter(slug=slug)
    print(category)
    categories = Category.objects.all()
    products = Product.objects.filter(category__in=category)
    print(products)
    context = {
        "products": products,
        "categories": categories
    }

    return render(request, 'products_list.html', context)
