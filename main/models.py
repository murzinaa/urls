import random
import string

from django.core import validators
from django.db import models


class Url(models.Model):
    old = models.URLField(
        verbose_name='Старая ссылка',
        max_length=500,
        default='',
        validators=[validators.URLValidator()]
    )
    new = models.CharField('Новая ссылка', blank=True, max_length=20, unique=True)

    def __str__(self):
        return self.old

    def save(self, *args, **kwargs):
        if not self.new:
            self.new = ''.join([random.choice(string.digits + string.ascii_letters) for _ in range(5)])
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'
