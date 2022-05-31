from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext as _
# Create your models here.




class reserve (models.Model):

    name = models.CharField(_("نام و نام خانوادگی"), max_length=50)
    email = models.EmailField(_("ایمیل"), max_length=254)
    phone = models.IntegerField(_("شماره تلفن"))
    number = models.IntegerField(_("تعداد "))
    date = models.DateField(_("تاریخ"), auto_now=True)
    time = models.TimeField(_("ساعت"), auto_now=True)
    
    class Meta():
        verbose_name = 'رزرو'
        verbose_name_plural = 'رزرو ها'

    
    def __str__(self):
        return self.name
    
