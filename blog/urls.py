from django.urls import path
from .views import Blog , detail ,category , search

app_name = 'blog'
urlpatterns = [
    path('' , Blog , name = 'blog'),
    path('<int:slug>/' , detail , name = 'detail'),
    path('category/<slug:slug>/' , category , name = 'category'),
    path('search/' , search , name = 'search'),
]
