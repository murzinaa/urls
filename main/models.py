from django.db import models
import random
import string
# from django.shortcuts import redirect
from django.core import validators

# создание моделей


class Url(models.Model):
    # указание класса полей и их ограничений
    old = models.URLField('Старая ссылка', max_length=500, default='',
                          validators=[validators.URLValidator()])
    new = models.CharField('Новая ссылка', blank=True, max_length=20, unique=True)

    def __str__(self):
        return self.old

    # функция, которая проверяет поле на пустоту и генерирует рандомную ссылку
    def save(self, *args, **kwargs):
        if not self.new:
            self.new = ''.join([random.choice(string.digits + string.ascii_letters) for _ in range(5)])
        super(Url, self).save(*args, **kwargs)  # Сохраняем запись, вызвав унаследованный метод


'''    def proverka(self, *args, **kwargs):
        if self.old:
            if not Url.objects.filter(old=self):
                return redirect('/about')
            else:
                super(Url, self).proverka(*args, **kwargs)'''