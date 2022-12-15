from django.db import models

class Ingredients(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)
    unit = models.CharField(max_length=50)
    unit_price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )

    def __str__(self):
        return f'{self.name.title()} - {self.quantity}'

class MenuItems(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )
    
    def __str__(self):
        return f'{self.title.title()} - ${self.price}'

class RecipeRequirements(models.Model):
    ingredient = models.ForeignKey(
        Ingredients,
        on_delete=models.CASCADE
    )
    menu_item = models.ForeignKey(
        MenuItems,
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.ingredient.name.title()} for {self.menu_item.title.title()}, total of {self.quantity}"

class Purchases(models.Model):
    menu_item = models.ForeignKey(
        MenuItems,
        on_delete=models.CASCADE
    )
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.menu_item.title.title()}: {self.timestamp}"