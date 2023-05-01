from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from .models import Manga, Category, Rating, MangaPage


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

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'manga', 'rating', 'created_at')
    list_filter = ('user', 'manga', 'created_at')
    search_fields = ('user__username', 'manga__title')
    ordering = ('-created_at',)


@admin.register(MangaPage)
class MangaPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'manga', 'page_number', 'image')
    list_filter = ('manga',)
    search_fields = ('manga__title', 'page_number')
    ordering = ('manga', 'page_number')