from django.urls import path

from . import views

app_name = 'userpart'

urlpatterns = [
    path('', views.index),
    path('',userpart.views.login_func, name='login'),
    path('',userpart.views.logout, name='logout'),
]