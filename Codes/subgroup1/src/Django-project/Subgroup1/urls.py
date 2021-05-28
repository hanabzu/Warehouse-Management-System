from django.contrib import admin
from django.urls import path
import userpart.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',userpart.views.home, name="home")
]
