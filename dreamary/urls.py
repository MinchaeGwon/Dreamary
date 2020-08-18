from django.contrib import admin
from django.urls import path
import dreamaryapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dreamaryapp.views.home, name='home')
]
