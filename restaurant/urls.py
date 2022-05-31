from django.urls import path
from .views import (home , detail , food_list , 
                    master_list_food , category_list , search , FavoriteFood)
app_name = 'food'
urlpatterns = [
    path('' , home , name = 'home'),
    path('<int:id>/' , detail , name = 'detail'),
    path('list/' , food_list , name = 'food-list'),
    path('master-chef/<slug:slug>' , master_list_food , name = 'master_food'),
    path('category/<slug:slug>' , category_list , name = 'category'),
    path('search/' , search , name = 'search'),
    path('favorite/<int:id>/' , FavoriteFood , name = 'favorite'),
]

