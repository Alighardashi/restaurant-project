from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.utils import timezone
from django.db import models
# Create your models here.


class Category(models.Model):
    title = models.CharField(_(" عنوان دسته بندی"), max_length=50)
    slug = models.SlugField(_("آدرس دسته بندی "))
    
    class Meta():
        verbose_name = 'دسته بندی'
        verbose_name_plural = ' دسته بندی ها'
    
    def __str__(self):
        return self.title



class blog(models.Model):
    title = models.CharField(_("عنوان"), max_length=50)
    slug = models.SlugField(_("آدرس"))
    description = models.TextField(_("توضیحات"))
    created = models.DateTimeField(_("زمان انتشار"), default = timezone.now)
    photo = models.ImageField(_("عکس"), upload_to='media/', height_field=None, width_field=None, max_length=None)
    author = models.ForeignKey(User,verbose_name=_("نویسنده"), related_name='blog' ,on_delete=models.SET_NULL , null=True)
    category = models.ForeignKey("Category", related_name='blog' , verbose_name=_("دسته بندی"), on_delete=models.SET_NULL, null=True)
    
    class Meta():
        verbose_name = 'وبلاگ'
        verbose_name_plural = 'وبلاگ ها'
    
    def __str__(self) :
        return self.title
    
    
    def photo_tag(self):
        return format_html("<img width='100px' style='border-radius:7px;' src='{}'>".format(self.photo.url))
    photo_tag.short_description='عکس مقاله'


class Comments(models.Model):
    Article = models.ForeignKey("blog", verbose_name=_("مقاله"), related_name='article' , on_delete=models.CASCADE)
    name = models.CharField(_(" نام و نام خانوادگی"), max_length=50) 
    email = models.EmailField(_("آدرس ایمیل"), max_length=254)
    message = models.TextField(_("نظر"))
    created = models.DateTimeField(_("زمان انتشار"), auto_now=False, auto_now_add=True)
    
    
    class Meta():
        verbose_name = 'نظر'
        verbose_name_plural = ' نظرات'
    
    def __str__(self) :
        return self.email
    