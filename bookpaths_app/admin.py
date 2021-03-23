from django.contrib import admin

from .models import User, Category
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(User)

class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
        exclude = ('id',)
        import_id_fields = ['name',]

@admin.register(Category)
class PropertyAdmin(ImportExportModelAdmin):
    resource_class  =   CategoryResource