from django.contrib import admin
from django.urls import path, include
import userpart.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userpart/', include('userpart.urls')),
    path('', userpart.views.home, name='home'),
    path('login/',userpart.views.login, name='login'),
    path('view/',userpart.views.acceptUsers, name='acceptUsers'),
    #path('free/',userpart.views.free, name='free'),
    #path('logout/',userpart.views.logout, name='logout'),
    #path('signup/', userpart.views.signup, name='signup'),
    #path('dosignup/', userpart.views.dosignup, name='dosignup'),
]
