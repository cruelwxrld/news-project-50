# news/models.py
from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок',
    )

    content = models.TextField(
        verbose_name='Содержимое',
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='articles',
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления',
    )

    is_published = models.BooleanField(
        default=False,
        verbose_name='Опубликовано',
    )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['is_published', 'created_at']),
            models.Index(fields=['author', 'created_at']),
        ]

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Название категории',
    )

    slug = models.SlugField(
        max_length=255,
        unique=True,
        verbose_name='URL',
    )

    articles = models.ManyToManyField(
        Article,
        verbose_name='Статьи',
        related_name='categories',
        blank=True,
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name