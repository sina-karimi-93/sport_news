
from django.urls import path, re_path
from .views import gallery_list, gallery_detail

app_name = 'gallery'

urlpatterns = [
    path('', gallery_list, name='gallery_list'),
    re_path(r'(?P<slug>[-\w]+)/', gallery_detail, name='gallery_detail'),
]