from django.urls import path, re_path
from .views import product_list, product_detail,product_category

app_name = 'products'

urlpatterns = [
    path('', product_list, name='product_list'),

    re_path(r'(?P<slug>[-\w]+)/جزییات/', product_detail, name='product_detail'),

    path('<int:pk>/دسته-بندی-ها/', product_category, name='product_category'),

]
