
from django.urls import path, re_path
from .views import article_list, article_detail
app_name = 'articles'

urlpatterns = [
    path('', article_list, name='article_list'),
    re_path(r'(?P<slug>[-\w]+)/', article_detail, name='article_detail'),

]
