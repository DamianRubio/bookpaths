import django_filters
from django import forms

from .models import BookPath, Category


class BookPathFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')
    description = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter()
    category = django_filters.ModelMultipleChoiceFilter(
        queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple)
    followers = django_filters.NumberFilter(field_name='follow_count', lookup_expr='gt')

    class Meta:
        model = BookPath
        exclude = []
