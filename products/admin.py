from django.contrib import admin
from .models import Product, Category, Ingredients, Custom_burger

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class IngredientsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'cyo',
        'cat',
    )


class Custom_burgerAdmin(admin.ModelAdmin):
    list_display = (
        'custom_name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Ingredients, IngredientsAdmin)
admin.site.register(Custom_burger, Custom_burgerAdmin)
