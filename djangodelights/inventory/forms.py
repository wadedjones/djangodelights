from django import forms
from .models import (
    Ingredients,
    MenuItems,
    RecipeRequirements,
    Purchases
)

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredients
        fields = '__all__'

    def get_absolute_url(self):
        return '/'

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItems
        fields = '__all__'

    def get_absolute_url(self):
        return '/'