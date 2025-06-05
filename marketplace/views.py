from django.shortcuts import render, get_object_or_404
from .models import Furniture
import random



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
    
    # Récupère les autres meubles sauf celui en cours
    other_furnitures = Furniture.objects.exclude(id=id)

    # Choisis 2 meubles aléatoires
    random_furnitures = random.sample(list(other_furnitures), min(2, other_furnitures.count()))

    return render(request, 'furniture_detail.html', {
        'furniture': furniture,
        'random_furnitures': random_furnitures
    })
