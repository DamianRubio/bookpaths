import django_filters
from django import forms

from .models import BookPath, Category


class BookPathFilter(django_filters.FilterSet):
    name = django_filters.CharFilter()
    category = django_filters.ModelMultipleChoiceFilter(
        queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = BookPath
        exclude = ['description', 'author', 'follow_count']
