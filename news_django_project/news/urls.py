from django.urls import path
from .views import home, article_detail, category_articles

urlpatterns = [
    path('', home, name='home'),
    path('article/<int:article_id>/', article_detail, name='article_detail'),
    path('category/<slug:category_slug>/', category_articles, name='category_articles'),
]