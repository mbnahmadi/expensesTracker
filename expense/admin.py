from django.contrib import admin
from .models import CategoryModel, ExpenseModel

# Register your models here.

class CategoryAminModel(admin.ModelAdmin):
    list_display = ['title', 'status']


class ExpenseAdminModel(admin.ModelAdmin):
    list_display = ['user', 'title', 'category', 'expense', 'status', 'created_at', 'updated_at']    


admin.site.register(CategoryModel, CategoryAminModel)
admin.site.register(ExpenseModel, ExpenseAdminModel)