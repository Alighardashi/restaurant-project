from django.contrib.auth import views
from django.urls import path
from .views import home , CreateFood , UpdateFood , DeleteFood , profile , PasswordChange
app_name = 'account'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('password_change/', PasswordChange.as_view(), name='password_change'),
    path('password_change_done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

urlpatterns +=[
    path('',home, name='home'),
    path('create/',CreateFood.as_view(), name='create'),
    path('update/<int:pk>',UpdateFood.as_view(), name='update'),
    path('delete/<int:pk>',DeleteFood.as_view(), name='delete'),
    path('profile/',profile.as_view(), name='profile'),
    ]