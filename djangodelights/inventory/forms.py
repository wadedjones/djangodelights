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
        widgets = {
            'name': forms.TextInput(attrs={
                'class':'form-control',
                'id':'name-form'
            }),
            'quantity': forms.TextInput(attrs={
                'class':'form-control',
                'id':'quantity-form'
            }),
            'unit': forms.TextInput(attrs={
                'class':'form-control',
                'id':'unit-form'
            }),
            'unit_price': forms.TextInput(attrs={
                'class':'form-control',
                'id':'unit-price-form'
            })
        }

    def get_absolute_url(self):
        return '/'

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItems
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class':'form-control',
                'id':'title-form'
                }),
            'price': forms.NumberInput(attrs={
                'class':'form-control',
                'id':'price-form'
                })
        }

    def get_absolute_url(self):
        return '/'

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchases
        fields = '__all__'