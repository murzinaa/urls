from django.contrib import admin
from .models import Url


class UrlAdmin(admin.ModelAdmin):
    list_display = ('old', 'new')  # отображение полей в бд


admin.site.register(Url, UrlAdmin)  # регистрация базы данных на странице администратора
