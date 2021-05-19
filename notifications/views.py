from django.shortcuts import render, get_object_or_404
from .models import Notification
# Create your views here.

1
def notification_list(request):
    notifications = Notification.objects.get_active_notifications()
    context = {
        "notifications": notifications
    }

    return render(request, 'notifications_list.html', context)


# def notification_detail(request, pk, slug):
#     notification = get_object_or_404(Notification, id=pk, slug=slug)
#     context = {
#         'notification': notification
#     }
#
#     return render(request, 'notifications_detail.html', context)

