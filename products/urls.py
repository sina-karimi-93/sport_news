from django.urls import path
from .views import product_list, product_detail, product_category

app_name = 'products'

urlpatterns = [
    path('', product_list, name='product_list'),
    path('<int:pk>/<slug:slug>/', product_detail, name='product_detail'),
    # path('<int:pk>/<slug:slug>/', product_detail, name='product_detail'),
    path('<slug:slug>/', product_category, name='product_category'),

]
