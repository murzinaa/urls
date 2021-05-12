from django.shortcuts import render, redirect
from .models import Url
from .forms import UrlForm
from django.http import HttpRequest, HttpResponse
# from django.core.exceptions import ValidationError


# Create your views here.
# # функция, которая вызывается при переходе на страницу "Главная"
def index(request):
    new_link = ''  # переменная, куда будет помещена новая ссылка
    # обработка кнопки "Выполнить!"
    if request.method == 'POST':
        form = UrlForm(request.POST)
        error = ''  # переменная, в которой будет текст об ошибке
        #  проверка формы на валидность
        if not form.is_valid():
            error = f'Ошибка: возможно Вы ввели несуществующую ссылку или такое имя новой ссылки уже существует! Введите другое имя для ссылки.'
            # form = form.clean()
            form = UrlForm()
            return render(request, 'main/index.html', {'form': form, 'error': error})  # вывод сообщения об ошибке

        else:

            form.save()  # сохранение данных из формы в БД
            new_link = str(f'{request.get_host()}/{form.save().new}')  # полный адрес новой ссылки
            n_link = str(f'{form.save().new}')  # адрес без домена
            return render(request, 'main/result.html', {'tasks': new_link, 'links': n_link})  # вывод данных о короткой ссылке
    form = UrlForm()
    context = {
        'form': form}

    return render(request, 'main/index.html', context)  # возвращает html шаблон вместе с формой


# функция, которая вызывается при переходе на страницу "Про нас"
def about(request):
    # обработка кнопки для перехода на главную страницу
    if request.method == 'POST':
        return redirect('/')
    return render(request, 'main/about.html')  # возвращает html шаблон


# функция, которая перехватывает ссылку и перенаправляет на нужную страницу(делает редирект)
def way(request):
    t = str(HttpRequest.get_full_path(request))  # забирает ссылку методом get_full_path()
    link1 = Url.objects.get(new=t[1:])  # забирает из БД старую ссылку по ключу новой
    return redirect(str(link1))  # перенаправляет пользователя по ссылке, которая хранится в переменной link1


# функция, которая вызывается при переходе на страницу "Как пользоваться"
def howtouse(request):
    # обработка кнопки для перехода на главную страницу
    if request.method == 'POST':
        return redirect('/')
    return render(request, 'main/howtouse.html')  # возвращает html шаблон


# функция, которая вызывается при переходе на страницу "Бот"
def bot(request):
    # обработка кнопки для перехода на главную страницу
    if request.method == 'POST':
        return redirect('/')
    return render(request, 'main/bot.html')  # возвращает html шаблон
