from django.shortcuts import render, get_object_or_404

from order.forms import UserNewOrderFOrm
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


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    new_order_form = UserNewOrderFOrm(request.POST or None, initial={'product_id': product.id})
    product_gallery = ProductImage.objects.filter(product=product)
    products = Product.objects.get_active_products()[0:6]
    context = {
        'product': product,
        "product_gallery": product_gallery,
        "products": products,
        'new_order_form': new_order_form
    }

    return render(request, 'products_detail.html', context)


def product_category(request, pk):
    category = Category.objects.filter(id=pk)
    categories = Category.objects.all()
    products = Product.objects.filter(category__in=category)
    context = {
        "products": products,
        "categories": categories,
        "category_title": category
    }
    print(category)
    return render(request, 'products_list.html', context)
