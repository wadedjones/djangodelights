from django.db import models

class Ingredients(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)
    TABLESPOON = 'tbsp'
    TEASPOON = 'tsp'
    CUP = 'cup'
    QUART = 'qt'
    PINT = 'pt'
    GALLON = 'gal'
    MEASUREMENT_CHOICES = [
        (TABLESPOON, 'tablespoon'),
        (TEASPOON, 'teaspoon'),
        (CUP, 'cup'),
        (QUART, 'quart'),
        (PINT, 'pint'),
        (GALLON, 'gallon')
    ]
    unit = models.CharField(
        max_length=4,
        choices=MEASUREMENT_CHOICES,
        default=TEASPOON
    )
    unit_price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )

class MenuItems(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )