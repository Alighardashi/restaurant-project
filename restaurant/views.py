from .models import Foods , MasterChef , Category , Comments
from django.shortcuts import get_object_or_404, redirect
from django.core.paginator import Paginator
from django.shortcuts import render
from .forms import CommentForm
from blog.models import Category as CAT

# Create your views here.

def home(request):
    MASTER = MasterChef.objects.all()
    FOODS = Foods.objects.all().order_by('created')[:6]
    CATEGORY = Category.objects.all()
    BLOG_CATEGORY = CAT.objects.all()
    
    context = {
        'foods' : FOODS ,
        'master': MASTER ,
        'Category' : CATEGORY ,
        'blogs_category' : BLOG_CATEGORY ,
    }
    return render (request , 'foods/home.html' , context)

def detail(request,id):
    
    FOODS = get_object_or_404(Foods , id=id)
    recent = Foods.objects.all().order_by("created")[:4]
    CATEGORY = Category.objects.all()
    comments = Comments.objects.all().filter(food=FOODS)
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data ["name"]
            new_email = form.cleaned_data ["email"]
            new_message = form.cleaned_data ["message"]
            
            new_comment = Comments(food=FOODS ,name = new_name ,email = new_email ,message = new_message)
            new_comment.save()
            
    context = {
        'foods' : FOODS ,
        'recent' : recent ,
        'category' : CATEGORY ,
        'comment' : comments ,
    }
    return render (request , 'foods/detail.html' , context)

def food_list(request):
    
    FOOD = Foods.objects.all()
    paginator = Paginator(FOOD, 6) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'food_list':page_obj
    }
    return render (request , 'foods/food_list.html' , context)

def master_list_food (request , slug):
    
    Food_Master = get_object_or_404(MasterChef , slug = slug)
    
    context = {
        'food_master':Food_Master
    }
    return render (request , 'foods/master_list_food.html' , context)


def category_list(request , slug):
    
    listt = get_object_or_404 (Category , slug = slug)
    
    context = {
        'LIST' : listt
    }
    return render (request , 'foods/category_list.html' , context)

def search (request):
    if request.method == "GET":
        rec_clinet = request.GET.get("search")
    FOOD = Foods.objects.filter(name__icontains = rec_clinet)
    
    context = {
        'food_list' : FOOD
    }
    
    return render (request , 'foods/food_list.html' , context)


def FavoriteFood (request , id):
    food=Foods.objects.get(id=id)
    is_favorite = False
    if food.favorite.filter(id=request.user.id).exists():
        food.favorite.remove(request.user)
        is_favorite = False
    else:
        food.favorite.add(request.user)
        is_favorite = True
    return redirect ("food:home")