from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            'brand', 'model', 'year', 'engine_volume', 'fuel_type',
            'transmission', 'power', 'mileage', 'price_china',
            'price_belarus', 'description', 'features', 'main_image',
            'image_1', 'image_2', 'is_available'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'features': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Например: климат-контроль, парктроники, камера, кожаный салон'
            }),
            'year': forms.NumberInput(attrs={'min': 2000, 'max': 2024}),
        }
        help_texts = {
            'price_belarus': 'Рассчитайте с учетом: цена в Китае + доставка + таможня + наши услуги',
        }