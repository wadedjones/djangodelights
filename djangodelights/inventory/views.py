from django.shortcuts import render, redirect, get_object_or_404
from .forms import (
    IngredientForm,
    MenuItemForm,
    PurchaseForm
)
from .models import (
    Ingredients,
    MenuItems,
    RecipeRequirements,
    Purchases
)
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'inventory/home.html')

@login_required
def ingredient_list(request):
    ingredients = Ingredients.objects.all()
    context = {'ingredients': ingredients}
    return render(request, 'inventory/ingredient_list.html', context)

@login_required
def add_ingredient(request):
    form = IngredientForm()
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(ingredient_list)
    
    context = {'form': form}
    return render(request, 'inventory/add_ingredient.html', context)

@login_required
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

@login_required
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

@login_required
def add_menu_item(request):
    form = MenuItemForm()
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory:menulist')

    context = {'form': form}
    return render(request, 'inventory/add_menu_item.html', context)

@login_required
def edit_menu_item(request, pk):
    menu_item = MenuItems.objects.get(id=pk)
    form = MenuItemForm(instance=menu_item)
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES, instance=menu_item)
        if form.is_valid():
            form.save()
            return redirect('inventory:menulist')

    context = {'menu_item': menu_item, 'form': form}
    return render(request, 'inventory/edit_menu_item.html', context)

@login_required
def delete_menu_item(request, pk):
    menu_item = MenuItems.objects.get(id=pk)
    if request.method == 'POST':
        menu_item.delete()
        return redirect(menu_list)

    context = {'menu_item': menu_item}
    return render(request, 'inventory/delete_menu_item.html', context)

@login_required
def recipe_list(request, pk):
    menu_item = get_object_or_404(MenuItems, pk=pk)
    rr = RecipeRequirements.objects.all()
    context = {'menu_item': menu_item, 'rr': rr}
    return render(request, 'inventory/recipes.html', context)

@login_required
def purchase_item(request, pk):
    menu_item = MenuItems.objects.get(id=pk)
    if request.method == 'POST':
        if menu_item.is_available():
            purchase = Purchases(menu_item=menu_item)
            purchase.save()
            for item in purchase.menu_item.reciperequirements_set.all():
                ingredient = item.ingredient
                ingredient.quantity -= item.quantity
                ingredient.save()
            return redirect('inventory:menulist')
        else:
            return render(request, 'inventory/out_of_stock.html')

    context = {'menu_item': menu_item}
    return render(request, 'inventory/purchase.html', context)

@login_required
def purchase_table(request):
    purchase_items = Purchases.objects.all()
    context = {'purchase_items': purchase_items}
    return render(request, 'inventory/purchase_table.html', context)