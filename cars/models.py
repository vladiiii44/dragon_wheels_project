from django.db import models

class Car(models.Model):
    FUEL_CHOICES = [
        ('petrol', 'Бензин'),
        ('diesel', 'Дизель'),
        ('hybrid', 'Гибрид'),
        ('electric', 'Электро'),
    ]
    
    TRANSMISSION_CHOICES = [
        ('manual', 'Механика'),
        ('automatic', 'Автомат'),
        ('cvt', 'Вариатор'),
    ]
    
    # Основная информация
    brand = models.CharField('Марка', max_length=100)
    model = models.CharField('Модель', max_length=100)
    year = models.IntegerField('Год выпуска')
    
    # Технические характеристики
    engine_volume = models.DecimalField('Объем двигателя (л)', max_digits=3, decimal_places=1, default=1.6)
    fuel_type = models.CharField('Тип топлива', max_length=20, choices=FUEL_CHOICES, default='petrol')
    transmission = models.CharField('Коробка передач', max_length=20, choices=TRANSMISSION_CHOICES, default='automatic')
    power = models.IntegerField('Мощность (л.с.)', default=150)
    mileage = models.IntegerField('Пробег (км)', default=0)
    
    # Цены
    price_china = models.DecimalField('Цена в Китае ($)', max_digits=10, decimal_places=2, default=25000)
    price_belarus = models.DecimalField('Цена в Беларуси ($)', max_digits=10, decimal_places=2, default=32000)
    
    # Описание и особенности
    description = models.TextField('Описание', blank=True, 
        default='Прямая поставка из Китая. Отличное состояние.')
    features = models.TextField('Особенности', blank=True,
        default='Климат-контроль, камера заднего вида, парктроник')
    
    # Фотография
    image = models.ImageField('Фотография', upload_to='cars/', blank=True, null=True)
    
    # Статус
    is_available = models.BooleanField('В наличии', default=True)
    created_at = models.DateTimeField('Дата добавления', auto_now_add=True)
    
    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
