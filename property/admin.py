from django.contrib import admin

from .models import (Property, Category, Reserve)

class PropertyAdmin(admin.ModelAdmin):
    list_display = ['name', 'property_type', 'location', 'category']
    search_fields = ('name', 'property_type')
    list_filter = ['category']

admin.site.register(Property, PropertyAdmin)
admin.site.register(Category)
admin.site.register(Reserve)