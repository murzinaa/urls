from django.urls import path, re_path
from . import views

# отслеживание переходов по страницам
urlpatterns = [
    path('', views.index),  # на главную
    path('about', views.about),  # на страницу "Про нас"
    path('howtouse', views.howtouse),  # на страницу "Как пользоваться"
    path('bot', views.bot),  # на страницу "Бот"
    re_path('.*', views.way),  # отслеживание переходов на все страницы (редирект)
]
