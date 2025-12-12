from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Article, Category


def home(request):
    search_query = request.GET.get('search', '')
    articles = Article.objects.filter(is_published=True)

    if search_query:
        articles = articles.filter(
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query)
        )

    articles = articles.order_by('-created_at')
    context = {
        'articles': articles,
        'search_query': search_query,
    }
    return render(request, 'news/index.html', context)


def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id, is_published=True)
    context = {'article': article}
    return render(request, 'news/article_detail.html', context)


def category_articles(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    articles = Article.objects.filter(
        categories=category,
        is_published=True
    ).order_by('-created_at')

    paginator = Paginator(articles, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'category': category,
        'page_obj': page_obj,
        'articles': page_obj.object_list,
    }
    return render(request, 'news/category.html', context)