from django.contrib import admin
from .models import (
    Ingredients,
    MenuItems,
    RecipeRequirements,
    Purchases
)

admin.site.register(Ingredients)
admin.site.register(MenuItems)
admin.site.register(RecipeRequirements)
admin.site.register(Purchases)