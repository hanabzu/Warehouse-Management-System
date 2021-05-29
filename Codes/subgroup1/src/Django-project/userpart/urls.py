from django.urls import path
from . import views

app_name = 'userpart'

urlpatterns = [

    #path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('dosignup/', views.dosignup, name='dosignup'),
    path('logout/', views.logout, name='logout'),

]