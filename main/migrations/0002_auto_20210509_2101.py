# Generated by Django 3.1.7 on 2021-05-09 18:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='new',
            field=models.CharField(blank=True, max_length=20, unique=True, verbose_name='Новая ссылка'),
        ),
        migrations.AlterField(
            model_name='url',
            name='old',
            field=models.URLField(default='', max_length=500, validators=[django.core.validators.URLValidator()], verbose_name='Старая ссылка'),
        ),
    ]
