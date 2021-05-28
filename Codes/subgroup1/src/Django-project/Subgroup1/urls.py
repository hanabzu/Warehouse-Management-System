from django.contrib import admin
from django.urls import path
import userpart.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',userpart.views.main, name="main"),
    path('',userpart.views.login_func, name="Login"),
    path('',userpart.views.logout, name="Logout"),
]
