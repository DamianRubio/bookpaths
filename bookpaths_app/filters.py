import django_filters
from django import forms

from .models import BookPath, Category, Book


class BookPathFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')
    description = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter()
    category = django_filters.ModelMultipleChoiceFilter(
        queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple)
    followers = django_filters.NumberFilter(
        field_name='follow_count', lookup_expr='gt')

    class Meta:
        model = BookPath
        exclude = []


class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='iexact')
    author = django_filters.CharFilter(lookup_expr='icontains')
    publisher = django_filters.CharFilter(
        field_name='publishers', lookup_expr='icontains')
    number_of_pages = django_filters.NumberFilter(
        field_name='number_of_pages', lookup_expr='lt')

    class Meta:
        model = Book
        exclude = ['isbn_10', 'isbn_13', 'cover']
