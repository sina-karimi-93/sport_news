from django.urls import path

from order.views import add_user_order, user_open_order, remove_order_detail

app_name = 'order'
urlpatterns = [
    path('add-user-order', add_user_order, name='add_user_order'),
    path('سبد-خرید', user_open_order, name='user_open_order'),
    path('remove-order-detail/<detail_id>', remove_order_detail),
]
