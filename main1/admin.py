from django.contrib import admin
from .models import Category, Product, Order, OrderItem


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    fields = ['product', 'quantity']

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)
admin.site.register(Order,OrderAdmin)
# admin.site.register(OrderItem)