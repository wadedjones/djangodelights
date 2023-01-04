from django.urls import path
from . import views

app_name = 'inventory'
urlpatterns = [
    path('', views.home, name='home'),
    path('ingredient_list', views.ingredient_list, name='ingredientlist'),
    path('add_ingredient', views.add_ingredient, name='addingredient'),
    path('edit_ingredient/<str:pk>', views.edit_ingredient, name='editingredient'),
    path('delete_ingredient/<str:pk>', views.delete_ingredient, name='deleteingredient'),
    path('menu_list', views.menu_list, name='menulist'),
    path('add_menu_item', views.add_menu_item, name='addmenuitem'),
    path('edit_menu_item/<str:pk>', views.edit_menu_item, name='editmenuitem'),
    path('delete_menu_item/<str:pk>', views.delete_menu_item, name='deletemenuitem'),
    path('recipe_list/<str:pk>', views.recipe_list, name='recipelist'),
    path('purchase/<str:pk>', views.purchase_item, name='purchaseitem'),
    path('purchase_table', views.purchase_table, name='purchasetable')
]