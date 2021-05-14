from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # переход на страницу администратора
    path('', include('main.urls')),  # подключает urlpatterns из файла main.urls
]
