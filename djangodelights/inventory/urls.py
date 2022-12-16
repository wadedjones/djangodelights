from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ingredient_list/', views.ingredient_list, name='ingredientlist'),
    path('add_ingredient/', views.add_ingredient, name='addingredient'),
    path('edit_ingredient/<str:pk>', views.edit_ingredient, name='editingredient')
]