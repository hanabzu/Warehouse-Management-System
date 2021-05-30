from django.urls import path
from . import views

app_name = 'userpart'

urlpatterns = [

    #path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('success/', views.dosignup, name='dosignup'),
    path('logout/', views.logout, name='logout'),
    path('<str:tA_id>/', views.viewTempAccountInfo, name= 'viewTempAccountInfo'),
    path('progressSuccess/', views.progressSuccess, name='progressSuccess'),


]