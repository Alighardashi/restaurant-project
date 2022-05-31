from django import template
from blog.models import Category as CAT
from ..models import Category , MasterChef

register=template.Library()

@register.inclusion_tag('partials/category_navbar.html')
def category_navbar():
    return {
            "Category" : Category.objects.all(),
            "master" : MasterChef.objects.all(),
            'blogs_category' : CAT.objects.all()
    }