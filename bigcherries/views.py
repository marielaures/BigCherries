from django.shortcuts import render

from .models import Recipe

# Create your views here.
def recipes(request):
    recipes = [
        Recipe(name='Pâtes aux champis', content='bla bla'),
        Recipe(name='Quiche', content='some stuff'),
    ]
    return render(request, 'recipes.html', {'recipes': recipes})
