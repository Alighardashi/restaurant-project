from http.client import FORBIDDEN
from django.shortcuts import render
from restaurant.models import Foods
from .forms import ReservationForm
# Create your views here.

def reserve (request):
    Foodss=Foods.objects.all()
    reserve_form = ReservationForm()
    if request.method == "POST":
        reserve_form = ReservationForm(request.POST)
        if reserve_form.is_valid():
            reserve_form.save()
    else:
        reserve_form = ReservationForm()
    context = {
        'form':reserve_form,
        'foods':Foodss
    }
    
    return render (request , 'reservation/reserve.html' ,context)