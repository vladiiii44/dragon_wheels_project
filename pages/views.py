from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def contacts(request):
    context = {
        'phone': '+375 (29) 160-20-06',
        'email': 'info@dragonwheels.by',
        'address': 'г. Минск, пр. Независимости, 58',
        'work_hours': 'Пн-Пт: 9:00-19:00, Сб: 10:00-16:00',
    }
    return render(request, 'pages/contacts.html', context)