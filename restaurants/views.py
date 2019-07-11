from django.shortcuts import render
from .models import Restaurant

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):
    context = {
        "restaurants": Restaurant.objects.all()
    }
    return render(request, 'list.html', context)




def restaurant_detail(request, restaurant_id):
    context = {
        "restaurant": Restaurant.objects.get(id=1),
    }
    return render(request, 'detail.html', context)
