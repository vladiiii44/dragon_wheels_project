from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'year', 'price_belarus', 'is_available', 'created_at']
    list_filter = ['brand', 'year', 'is_available', 'fuel_type']
    search_fields = ['brand', 'model', 'description']
    list_editable = ['is_available', 'price_belarus']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('brand', 'model', 'year', 'description', 'features')
        }),
        ('Технические характеристики', {
            'fields': ('engine_volume', 'fuel_type', 'transmission', 'power', 'mileage')
        }),
        ('Цены', {
            'fields': ('price_china', 'price_belarus')
        }),
        ('Фотография', {
            'fields': ('image',)
        }),
        ('Статус', {
            'fields': ('is_available',)
        }),
    )
