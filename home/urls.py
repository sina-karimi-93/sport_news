from django.urls import path, re_path
from .views import news_list, news_detail, calculate_bmi, contact_us

app_name = 'news'

urlpatterns = [
    path('', news_list, name='news_list'),
    re_path(r'(?P<slug>[-\w]+)/جزییات/', news_detail, name='news_detail'),
    path('bmi', calculate_bmi, name='calculate_bmi'),
    path('contact-us', contact_us, name='contact_us')
]
