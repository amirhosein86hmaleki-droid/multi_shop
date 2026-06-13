from django.contrib import admin

from .import models
# from models import Product

# admin.site.register(models.Product)
class InformationAdmin(admin.StackedInline):
    model = models.Information


admin.site.register(models.Size)
admin.site.register(models.Color)

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'id',
        'quantity',
        'status',
    ]
    inlines = (InformationAdmin,)