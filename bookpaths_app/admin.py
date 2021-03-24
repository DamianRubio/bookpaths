from django.contrib import admin
from django.contrib.auth.hashers import make_password
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Category, User, BookPath


admin.site.register(BookPath)

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
