from django.shortcuts import render
from .models import Item, OrderItem, Order


def home(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "home.html", context)

def products(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "products.html", context)

def checkout(request):
 
    return render(request, "checkout.html")
