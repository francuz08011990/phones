from django.contrib import admin

from .models import Phones, Type


@admin.register(Phones)
class PhonesAdmin(admin.ModelAdmin):
    search_fields = ('brand',)
    list_filter = ('brand', )


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    fields = (
        'name_of_model', 'phone', 'price', 'image'
    )
    list_display = ('id', 'name_of_model', 'phone', 'price', )
    search_fields = ('name_of_model', )


