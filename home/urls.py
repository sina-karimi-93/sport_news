from django.urls import path, re_path
from .views import news_list, news_detail


app_name = 'news'

urlpatterns = [
    path('', news_list, name='news_list'),
    re_path(r'(?P<slug>[-\w]+)/جزییات/', news_detail, name='news_detail'),
]
