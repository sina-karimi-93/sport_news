from django.shortcuts import render, get_object_or_404
from .models import News
# Create your views here.


def news_list(request):
    news = News.objects.get_active_news()
    print(request.user)
    context = {
        "news": news
    }

    return render(request, 'news_list.html', context)


def news_detail(request, slug):
    single_news = get_object_or_404(News, slug=slug)
    context = {
        'single_news': single_news
    }

    return render(request, 'news_detail.html', context)
