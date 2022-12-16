from django.shortcuts import render, redirect
from .forms import (
    IngredientForm,
    MenuItemForm
)
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

def menu_list(request):
    menu_items = MenuItems.objects.all()
    context = {'menu_items': menu_items}
    return render(request, 'inventory/menu_list.html', context)

def add_menu_item(request):
    form = MenuItemForm()
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(menu_list)

    context = {'form': form}
    return render(request, 'inventory/add_menu_item.html', context)

def edit_menu_item(request, pk):
    menu_item = MenuItems.objects.get(id=pk)
    form = MenuItemForm(instance=menu_item)
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES, instance=menu_item)
        if form.is_valid():
            form.save()
            return redirect(menu_list)

    context = {'menu_item': menu_item, 'form': form}
    return render(request, 'inventory/edit_menu_item.html', context)

def delete_menu_item(request, pk):
    menu_item = MenuItems.objects.get(id=pk)
    if request.method == 'POST':
        menu_item.delete()
        return redirect(menu_list)

    context = {'menu_item': menu_item}
    return render(request, 'inventory/delete_menu_item.html', context)

def recipe_list(request):
    menu_item = MenuItems.objects.all()
    rr = RecipeRequirements.objects.all()
    context = {'menu_item': menu_item, 'rr': rr}
    return render(request, 'inventory/recipes.html', context)