from django.urls import path
from .views import reserve

app_name = 'reservation'
urlpatterns = [
    path ('' , reserve , name = 'reserve'),
]