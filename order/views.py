from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect

from products.models import Product
from .forms import UserNewOrderFOrm

# Create your views here.
from .models import Order, OrderDetail


@login_required
def add_user_order(request):
    new_order_form = UserNewOrderFOrm(request.POST or None)
    if new_order_form.is_valid():
        order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
        if order is None:
            order = Order.objects.create(owner_id=request.user.id, is_paid=False)

        product_id = new_order_form.cleaned_data.get('product_id')
        count = new_order_form.cleaned_data.get('count')
        try:
            int(count)
            if count < 1:
                count = 1
        except:
            count = 1
        product = Product.objects.filter(id=product_id).first()

        # check if has this item
        if order.orderdetail_set.filter(product_id=product_id):
            order.orderdetail_set.filter(product_id=product_id).update(count=count)
        else:
            order.orderdetail_set.create(product_id=product.id, price=product.price, count=count)
    return redirect('/products')


@login_required
def user_open_order(request, *args, **kwargs):
    context = {
        'order': None,
        'details': None,
        'total_price': 0,
        'total_count': 0
    }
    total_price = 0
    total_count = 0
    open_order: Order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    if open_order is not None:
        context['order'] = open_order
        context['details'] = open_order.orderdetail_set.all()
        context['total_price'] = open_order.get_total_price()
        context['total_count'] = open_order.get_total_count()
    return render(request, 'user_open_order.html', context)


@login_required
def remove_order_detail(request, *args, **kwargs):
    detail_id = kwargs.get('detail_id')
    if detail_id is not None:
        order_detail = OrderDetail.objects.get_queryset().get(id=detail_id, order__owner_id=request.user.id)
        if order_detail is not None:
            order_detail.delete()
            return redirect('/orders/سبد-خرید')
    raise Http404()
