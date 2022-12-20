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

def recipe_list(request, pk):
    menu_item = get_object_or_404(MenuItems, pk=pk)
    rr = RecipeRequirements.objects.all()
    context = {'menu_item': menu_item, 'rr': rr}
    return render(request, 'inventory/recipes.html', context)

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
            return redirect(menu_list)
        else:
            return render(request, 'inventory/out_of_stock.html')

    context = {'menu_item': menu_item}
    return render(request, 'inventory/purchase.html', context)

def total_purchases(request):
    purchases = Purchases.objects.all()
    context = {'purchases': purchases}
    return render(request, 'inventory/total_purchases.html', context)


def search_purchases(request):
    if request.accepts('application/json'):
        res = None
        item = request.POST.get('menuItem')
        qs = Purchases.objects.filter(Q(menu_item__title__icontains=item))
        if len(qs) > 0 and len(item) > 0:
            data = []
            for i in qs:
                mi = {
                    'pk': i.menu_item.pk,
                    'title': i.menu_item.title,
                    'price': i.menu_item.price,
                    'date': i.timestamp
                }
                data.append(mi)
            res = data
        else:
            res = 'No Menu Items found ...'
        return JsonResponse({'data': res})
    return JsonResponse({})

def search_recipe_list(request):
    if request.accepts('application/json'):
        res = None
        item = request.POST.get('recipe')
        qs = MenuItems.objects.filter(Q(title__icontains=item))
        print(qs)
        if len(qs) > 0 and len(item) > 0:
            data = []
            for i in qs:
                ri = {
                    'pk': i.pk,
                    'title': i.title,
                    'price': i.price
                }
                data.append(ri)
            res = data
        else:
            res = 'No menu items found...'
        return JsonResponse({'data': res})
    return JsonResponse({})