from django.shortcuts import render, get_object_or_404
from .models import Car

def car_list(request):
    # Показываем только автомобили из базы данных
    cars = Car.objects.filter(is_available=True)
    return render(request, 'cars/car_list.html', {'cars': cars})

def car_detail(request, id):
    # Показываем только автомобили из базы данных
    car = get_object_or_404(Car, id=id, is_available=True)
    return render(request, 'cars/car_detail.html', {'car': car})
