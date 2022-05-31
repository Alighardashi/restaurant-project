from dataclasses import fields
from .models import reserve
from django import forms

class ReservationForm(forms.ModelForm):
    class Meta:
        model = reserve
        fields = '__all__'