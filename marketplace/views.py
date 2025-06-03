from django.shortcuts import render, get_object_or_404
from .models import Furniture


# Create your views here.

def home(request):
    return render(request, 'index.html')

def gallerie(request):
    items = Furniture.objects.all()
    return render(request, 'gallerie.html', {'items': items})
    
def leistungen(request):
    return render(request, 'leistungen.html')

def fragen(request):
    return render(request, 'fragen.html')


def furniture_detail(request, id):
    furniture = get_object_or_404(Furniture, id=id)
    return render(request, 'furniture_detail.html', {'furniture': furniture})


