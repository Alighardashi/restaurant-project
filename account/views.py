from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from restaurant.models import Foods , MasterChef ,Comments
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView , PasswordResetView
from django.views.generic import CreateView , UpdateView , DeleteView
from django.shortcuts import  render
from reserve.models import reserve
# Create your views here.

@login_required
def home(request):
    FOOD=Foods.objects.all()
    RESERVE = reserve.objects.all()
    MRCHEF = MasterChef.objects.all()
    COMMENTS = Comments.objects.all()
    context = {
        'reserve':RESERVE ,
        'foods':FOOD,
        'masterchef':MRCHEF,
        'message':COMMENTS,
        
    }
    return render (request , 'registration/home.html' , context)


class CreateFood(LoginRequiredMixin , CreateView):
    model = Foods
    fields = ['name' , 'description' , 'price' , 'photo' , 'ingredients' , 'master_chef' , 'created' , 'category']
    template_name = 'registration/create-update-food.html'
    
    
class UpdateFood(LoginRequiredMixin , UpdateView):
    model = Foods
    fields = ['name' , 'description' , 'price' , 'photo' , 'ingredients' , 'master_chef' , 'created' , 'category']
    template_name = 'registration/create-update-food.html'

    
    
class DeleteFood(LoginRequiredMixin , DeleteView):
    model = Foods
    success_url =reverse_lazy("account:home")
    template_name = 'registration/delete.html'
    
class profile(LoginRequiredMixin , UpdateView):
    model = User
    fields = ['username' , 'last_name' , 'first_name' , 'email' , 'is_staff']
    template_name = 'registration/profile.html'
    success_url =reverse_lazy("account:profile")
    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)
    
    
class PasswordChange(PasswordChangeView):
    success_url =reverse_lazy("account:password_change_done")
