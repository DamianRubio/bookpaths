import django_filters
from django import forms

from .models import BookPath, Category, Book


class BookPathFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')
    description = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter()
    category = django_filters.ModelMultipleChoiceFilter(
        queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple)
    followers = django_filters.NumberFilter(label='With more than X followers',
        field_name='follow_count', lookup_expr='gt')
    steps = django_filters.NumberFilter(label='With at most X steps', field_name='steps', lookup_expr='lte')

    o = django_filters.OrderingFilter(
        fields=(
            ('name', 'name'),
            ('author', 'author'),
            ('category', 'category'),
            ('follow_count', 'follow_count'),
            ('steps', 'steps'),
        ),

        field_labels={
            'follow_count': 'Followers',
            'steps':'Steps',
        }
    )

    class Meta:
        model = BookPath
        exclude = []


class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='iexact')
    author = django_filters.CharFilter(lookup_expr='icontains')
    publisher = django_filters.CharFilter(
        field_name='publishers', lookup_expr='icontains')
    number_of_pages = django_filters.NumberFilter(label='Less than X pages',
        field_name='number_of_pages', lookup_expr='lt')
    paths = django_filters.NumberFilter(label='Included in at least X paths', field_name='paths', lookup_expr='gte')

    o = django_filters.OrderingFilter(
        fields=(
            ('title', 'title'),
            ('author', 'author'),
            ('number_of_pages', 'number_of_pages'),
            ('paths', 'paths'),
        ),

        field_labels={
            'number_of_pages': 'Pages',
            'paths': 'Paths in which the book appears',
        }
    )

    class Meta:
        model = Book
        exclude = ['isbn_10', 'isbn_13', 'cover']
