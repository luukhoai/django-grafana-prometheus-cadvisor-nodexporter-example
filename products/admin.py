from django.contrib import admin
from reversion.admin import VersionAdmin

# Register your models here.

from .models import Products


class ProductsHistoryAdmin(VersionAdmin):
    list_display = ['name', 'price']
    search_fields = ['name']
    list_filter = ['price']


admin.site.register(Products, ProductsHistoryAdmin)