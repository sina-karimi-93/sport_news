from django.shortcuts import render, get_object_or_404
from .models import Article
# Create your views here.


def article_list(request):
    articles = Article.objects.get_active_articles()
    context = {
        "articles": articles
    }

    return render(request, 'article_list.html', context)


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    context = {
        'article': article
    }

    return render(request, 'article_detail.html', context)
