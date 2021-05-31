from django.contrib import admin
from django.urls import path, include
import userpart.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userpart/', include('userpart.urls')),
    path('', userpart.views.home, name='home'),
    path('2', userpart.views.home2, name='home2'),
    path('login/',userpart.views.login, name='login'),
    path('view/',userpart.views.acceptUsers, name='acceptUsers'),
    path('<str:A_id>/',userpart.views.logout, name='logout'),
]
