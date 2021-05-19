
from django.urls import path, include
from .views import gallery_list, gallery_detail

app_name = 'gallery'

urlpatterns = [
    path('', gallery_list, name='gallery_list'),
    path('<int:pk>/<slug:slug>', gallery_detail, name='gallery_detail'),
]