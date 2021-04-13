from django.contrib import admin
from django.contrib.auth.hashers import make_password
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import (Book, BookPath, BookPathFollow, BookPathStep, Category,
                     User)

admin.site.register(BookPathFollow)


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
        exclude = ('id',)
        import_id_fields = ['name', ]


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    resource_class = CategoryResource


class UserResource(resources.ModelResource):

    def before_import_row(self, row, **kwargs):
        value = row['password']
        row['password'] = make_password(value)

    class Meta:
        model = User


@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    resource_class = UserResource

class BookResource(resources.ModelResource):
    class Meta:
        model = Book
        exclude = ('id',)
        import_id_fields = ['isbn_10', ]


@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    resource_class = BookResource

class BookPathResource(resources.ModelResource):
    class Meta:
        model = BookPath


@admin.register(BookPath)
class BookPathAdmin(ImportExportModelAdmin):
    resource_class = BookPathResource

class BookPathStepResource(resources.ModelResource):
    class Meta:
        model = BookPathStep


@admin.register(BookPathStep)
class BookPathAdmin(ImportExportModelAdmin):
    resource_class = BookPathStepResource