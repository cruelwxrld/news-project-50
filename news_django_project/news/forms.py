from django import forms
from .models import Article

class ArticleSearchForm(forms.Form):
    search = forms.CharField(
        required=False,
        label='Поиск',
        widget=forms.TextInput(attrs={
            'placeholder': 'Введите заголовок для поиска...',
            'class': 'search-input'
        })
    )