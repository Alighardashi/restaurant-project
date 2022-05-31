from django.contrib import admin
from .models import Foods , MasterChef , Category , Comments , image
# Register your models here.



class FoodsAdmin(admin.ModelAdmin):
    list_display = ['name' , 'category' , 'price' , 'master_chef' , 'photo_tag']
    list_filter = ['category' , 'price' , 'master_chef' ]
    search_fields = ['category' , 'price' , 'master_chef']
    
admin.site.register(Foods , FoodsAdmin)




class MasterChefAdmin(admin.ModelAdmin):
    list_display = ['name','slug','old']
    list_filter = ['name' , 'slug' , 'old']
    search_fields = ['slug' , 'old' , 'name']
admin.site.register(MasterChef , MasterChefAdmin)




class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title' , 'slug']
    list_filter = ['title' , 'slug']
    search_fields = ['slug' , 'title']
admin.site.register(Category , CategoryAdmin)




class CommentAdmin(admin.ModelAdmin):
    list_display = ['name' , 'email']
    list_filter = ['email']
    search_fields = ['name' , 'email']
    
admin.site.register(Comments , CommentAdmin)

admin.site.register(image)






