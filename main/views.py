from django.shortcuts import render, redirect, get_object_or_404
from .models import Url
from .forms import UrlForm
from django.http import HttpRequest, HttpResponse
# from django.core.exceptions import ValidationError
from collections.abc import Callable
from django.views import View


# Create your views here.

'''def index(request):
    new_link = ''  # переменная, куда будет помещена новая ссылка
    # обработка кнопки "Выполнить!"

    if request.method == 'POST':
        form = UrlForm(request.POST)
        if 'main' in request.POST:
            return redirect('/')
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
    return render(request, 'main/bot.html')  # возвращает html шаблон'''


# класс, который вызывается при переходе на страницу "Главная"
class IndexView(View):

    index = 'main/index.html'
    result = 'main/result.html'
    # функция, которая возвращает шаблон index.html

    def get(self, request: HttpRequest):
        return render(request, self.index, {'form': UrlForm()})

    # обработка кнопки
    def post(self, request: HttpRequest):
        if 'main' in request.POST:
            return redirect('/')

        form = UrlForm(request.POST)
        # проверка формы на валидность
        if not form.is_valid():
            context = {
                'form': UrlForm(),
                'error': f'Ошибка: '
                         f'возможно Вы ввели несуществующую ссылку или такое имя новой ссылки уже существует! '
                         f'Введите другое имя для ссылки.'
            }
            return render(request, self.index, context)  # функция, которая возвращает шаблон index.html

        saved_form = form.save()  # сохранение формы в бд
        n_link = f'{saved_form.new}'
        new_link = f'{request.get_host()}/{n_link}'
        return render(request, self.result, {'tasks': new_link, 'links': n_link})  # функция, которая возвращает шаблон result.html


def redirect_to_main_if_post(function: Callable[[HttpRequest], HttpResponse]):
    # Декоратор, который упрощает редирект на главную страницу по методу POST
    def wrapper(request: HttpRequest) -> HttpResponse:
        return redirect('/') if request.method == 'POST' else function(request)
    return wrapper


# функция, которая вызывается при переходе на страницу "Про нас"
@redirect_to_main_if_post
def about(request: HttpRequest): return render(request, 'main/about.html')


# функция, которая вызывается при переходе на страницу "Как пользоваться"
@redirect_to_main_if_post
def how_to_use(request: HttpRequest): return render(request, 'main/howtouse.html')


# функция, которая вызывается при переходе на страницу "Бот"
@redirect_to_main_if_post
def bot(request: HttpRequest): return render(request, 'main/bot.html')


# функция, которая перехватывает ссылку и перенаправляет на нужную страницу(делает редирект)
def way(request: HttpRequest, link: str): return redirect(get_object_or_404(Url, new=link).old)
