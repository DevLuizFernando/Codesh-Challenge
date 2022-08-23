from django.contrib import admin
from OpenFoodFacts.models import Produto

class Produtos(admin.ModelAdmin):
    list_display = ('id', 'code', 'barcode', 'status', 'imported_t', 'url', 'product_name', 'quantity', 'categories', 
    'packaging', 'brands', 'image_url')
    list_display_links = ('id', 'product_name')
    search_fields = ('product_name',)
    list_per_page = 10
    ordering = ('id',)

admin.site.register(Produto, Produtos)