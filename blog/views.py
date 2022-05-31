from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from .models import blog , Category , Comments
from .forms import CommentsForm
# Create your views here.

def Blog(request):
    
    BLOG = blog.objects.all()
    paginator = Paginator(BLOG, 6) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    BLOG_LIST = paginator.get_page(page_number)
    
    context = {
        'blog_list':BLOG_LIST,
    }
    
    
    return render (request , 'blog/blog.html' , context)




def detail(request , slug):
    
    BLOG = get_object_or_404(blog , slug=slug)
    categoryy = Category.objects.all()
    comments = Comments.objects.all().filter(Article=BLOG)
    
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data['name']
            new_email = form.cleaned_data['email']
            new_message = form.cleaned_data['message']
            
            new_comment = Comments(Article = BLOG , name = new_name , email = new_email , message = new_message)
            new_comment.save()
            
    context = {
        'article' : BLOG ,
        'category' : categoryy,
        'recent' : blog.objects.all().order_by("created")[:5],
        'comment' : comments
        
    }
    
    
    return render (request , 'blog/detail.html' , context)




def category(request , slug):
    
    LIST_CATEGORY = get_object_or_404 (Category , slug = slug)
    
    context ={
        'L_category' : LIST_CATEGORY ,
    }
    
    
    return render (request , 'blog/category_list.html' , context)


def search (request):
    if request.method == "GET":
        rec_client = request.GET.get("search")
    BLOG_LIST = blog.objects.filter(title__icontains = rec_client)
    
    context = {
        'blog_list':BLOG_LIST,
    }
    return render (request , 'blog/blog.html' , context)
