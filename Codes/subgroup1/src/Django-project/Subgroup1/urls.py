from django.contrib import admin
from django.urls import path, include
import userpart.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userpart/', include('userpart.urls')),
]
