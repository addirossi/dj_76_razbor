from django.contrib import admin

from .models import Category, Product, Order, OrderItems


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


class OrderItemsInline(admin.TabularInline):
    model = OrderItems
    fields = ['product', 'quantity']
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemsInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItems)
