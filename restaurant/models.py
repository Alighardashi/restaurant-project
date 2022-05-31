from django.utils.translation import gettext as _
from django.utils.html import format_html
from django.utils import timezone
from django.contrib.auth.models import User 
from django.urls import reverse
from django.db import models

# Create your models here.
class MasterChef(models.Model):
    name = models.CharField(_("اسم"), max_length=50)
    old = models.IntegerField(_("سن"))
    slug = models.SlugField(_("شناسه"))
    
    class Meta():
        verbose_name = 'سرآشپز'
        verbose_name_plural = 'سرآشپز ها'

    def __str__(self):
        return self.name
    

class Category(models.Model):
    title = models.CharField(_("نام دسته بندی"), max_length=50)
    slug = models.SlugField(_("شناسه دسته بندی"))
    
    class Meta():
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        
    def __str__(self):
        return self.title



class Foods(models.Model):
    FOOD_CHOICES = (
        ("breakfast","صبحانه"),
        ("lunch","ناهار"),
        ("dinner","شام"),
        ("all","همه")
    )
    name = models.CharField(_(" نام "), max_length=50)
    description = models.TextField(_("  توضیحات  "))
    price = models.IntegerField(_("  قیمت  "))
    photo = models.ImageField(_("  عکس  "), upload_to='media/', height_field=None, width_field=None, max_length=None)
    ingredients = models.TextField(_("مواد لازم"))
    type_food = models.CharField(_("تایم غذا"), max_length=50 , choices=FOOD_CHOICES)
    master_chef = models.ForeignKey("MasterChef", related_name='food' ,verbose_name=_("سرآشپز"), on_delete=models.SET_NULL , null=True)
    created = models.DateTimeField(_("زمان انتشار"), default = timezone.now)
    category = models.ForeignKey("Category", verbose_name=_("دسته بندی"), related_name='food' ,on_delete=models.SET_NULL , null=True)
    favorite = models.ManyToManyField(User, blank=True ,verbose_name=_("علاقه مندی ها") , related_name='fa_user')
    
    class Meta:
        verbose_name = 'غذا'
        verbose_name_plural = 'غذا ها'

    def __str__(self):
        return self.name
    
    
    def get_absolute_url(self):
        return reverse("account:home")
    
    
    def photo_tag(self):
        return format_html("<img width='100px' style='border-radius:7px;' src='{}'>".format(self.photo.url))
    photo_tag.short_description='عکس غذا'


class Comments(models.Model):
    food = models.ForeignKey("Foods", verbose_name=_("غذا"), related_name='comments',  on_delete=models.CASCADE )
    name = models.CharField(_("نام و نام خانوادگی"), max_length=100)
    email = models.EmailField(_("آدرس ایمیل"), max_length=254)
    message = models.TextField(_("نظر"))

    
    class Meta():
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'
    
    def __str__(self):
        return self.email
    
    
class image(models.Model):
    food=models.ForeignKey(Foods, on_delete=models.CASCADE)
    photo=models.ImageField(upload_to='media/', blank=True)