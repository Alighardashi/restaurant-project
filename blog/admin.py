from django.contrib import admin
from .models import blog , Category , Comments
# Register your models here.

class AdminBlog(admin.ModelAdmin):
    
    list_display = ['title' ,'slug' ,'category' , 'author' ,'photo_tag']
    list_filter = ['slug' , 'category' , 'author']
    search_fields = ['title' , 'slug' , 'category' , 'author']
    
admin.site.register (blog , AdminBlog)



class AdminCategory(admin.ModelAdmin):
    
    list_display = ['title' , 'slug']
    list_filter = ['slug']
    search_fields = ['title' , 'slug']

admin.site.register (Category , AdminCategory)



class AdminComment(admin.ModelAdmin):
    
    list_display = ['name' , 'email']
    list_filter = ['email']
    search_fields = ['name' , 'email']

admin.site.register (Comments , AdminComment)