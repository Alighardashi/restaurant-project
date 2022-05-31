from django.contrib import admin
from .models import reserve #, Food
# Register your models here.

class ReserveAdmin(admin.ModelAdmin):
    list_display = ['name' , 'email' , 'phone' , 'number']
    list_filter = ['number']
    search_fields = ['time' , 'number']

admin.site.register(reserve , ReserveAdmin)
