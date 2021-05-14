from django.urls import path

from .views import IndexView, about, how_to_use, bot, way

urlpatterns = [
    path('', IndexView.as_view()),  # на главную
    path('about/', about),  # на страницу "Про нас"
    path('howtouse/', how_to_use),  # на страницу "Как пользоваться"
    path('bot/', bot),  # на страницу "Бот"
    path('<str:link>/', way),  # отслеживание переходов на все страницы (редирект)
]