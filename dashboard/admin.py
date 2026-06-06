from django.contrib import admin
from .models import Category, Product, Order


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_order', 'image_tag')
    list_editable = ('display_order',)

    def image_tag(self, obj):
        if obj.image:
            return '<img src="%s" width="50" height="50" style="object-fit:cover;border-radius:8px;" />' % obj.image.url
        return '<span style="color:#999">No image</span>'
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'image_tag')
    list_filter = ('category',)
    search_fields = ('name', 'description')

    def image_tag(self, obj):
        if obj.image:
            return '<img src="%s" width="50" height="50" style="object-fit:cover;border-radius:8px;" />' % obj.image.url
        return '<span style="color:#999">No image</span>'
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'quantity', 'amount', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('product_name', 'customer_name')
