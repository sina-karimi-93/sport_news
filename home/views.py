from django.shortcuts import render, get_object_or_404
from .models import News
from django.core.paginator import Paginator


# Create your views here.


def news_list(request):
    news = News.objects.get_active_news()
    last_five_news = news[0:5]

    paginator = Paginator(news, 6)  # Show 8 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "news": news,
        "last_news": last_five_news,
        "page_obj": page_obj
    }

    return render(request, 'news_list.html', context)


def news_detail(request, slug):
    single_news = get_object_or_404(News, slug=slug)
    context = {
        'single_news': single_news
    }

    return render(request, 'news_detail.html', context)
