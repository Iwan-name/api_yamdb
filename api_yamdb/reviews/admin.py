from django.contrib import admin

from .models import Category, Genre, Title


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    empty_value_display = '-пусто'


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    empty_value_display = '-пусто'


class TitleAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name',
                    'year',
                    'rating',
                    'description',
                    'genre',
                    'category')
    empty_value_display = '-пусто'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Genre, GenreAdmin)