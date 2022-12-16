from django.shortcuts import render, redirect
from .forms import IngredientForm
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
    form = IngredientForm()
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(ingredient_list)
    
    context = {'form': form}
    return render(request, 'inventory/add_ingredient.html', context)

def edit_ingredient(request, pk):
    ingredient = Ingredients.objects.get(id=pk)
    form = IngredientForm(instance=ingredient)
    if request.method == 'POST':
        form = IngredientForm(request.POST, request.FILES, instance=ingredient)
        if form.is_valid():
            form.save()
            return redirect(ingredient_list)
    
    context = {'ingredient': ingredient, 'form': form}
    return render(request, 'inventory/edit_ingredient.html', context)

def delete_ingredient(request, pk):
    ingredient = Ingredients.objects.get(id=pk)
    if request.method == 'POST':
        ingredient.delete()
        return redirect(ingredient_list)

    context = {'ingredient': ingredient}
    return render(request, 'inventory/delete_ingredient.html', context)