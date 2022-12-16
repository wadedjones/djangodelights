from django.shortcuts import render, redirect
from .forms import AddIngredient

from .models import (
    Ingredients,
    MenuItems,
    RecipeRequirements,
    Purchases
)

def home(request):
    return render(request, 'inventory/home.html')

def ingredient_list(request):
    ingredients = Ingredients.objects.all()
    context = {'ingredients': ingredients}
    return render(request, 'inventory/ingredient_list.html', context)

def add_ingredient(request):
    form = AddIngredient()
    if request.method == 'POST':
        form = AddIngredient(request.POST)
        if form.is_valid():
            form.save()
            return redirect(ingredient_list)
    
    context = {'form': form}
    return render(request, 'inventory/add_ingredient.html', context)