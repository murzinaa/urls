from django.contrib import admin
from .models import Url


@admin.register(Url) # регистрация базы данных на странице администратора
class UrlAdmin(admin.ModelAdmin):
    list_display = ('old', 'new')  # отображение полей в бд
