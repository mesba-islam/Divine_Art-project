from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display =('title', 'price', 'sku', 'category', 'modified_date', 'is_available')
    prepopulated_fields ={'slug': ('title',)}

admin.site.register(Product,ProductAdmin)