from django.contrib import admin
from .models import Products
# Register your models here.

admin.site.site_header="E-commerce"
admin.site.site_title="ABC Shopping"
admin.site.index_title="Manage ABC Shopping"


class ProductAdmin(admin.ModelAdmin):
    list_display=('title','price','discount_price','category')
    search_fields=('category',)
    fields=('title','price',)
    list_editable=('price',)

admin.site.register(Products,ProductAdmin)