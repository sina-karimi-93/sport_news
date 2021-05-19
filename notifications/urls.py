
from django.urls import path
from .views import notification_list
app_name = 'notifications'

urlpatterns = [
    path('', notification_list, name='notification_list'),
    # path('<int:pk>/<slug:slug>/', notification_detail, name='notification_detail'),

]
