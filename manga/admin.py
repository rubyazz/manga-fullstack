from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from .models import Manga, Category


@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'display_categories']
    filter_horizontal = ['categories']
    search_fields = ['title', 'author']
    
    def display_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}