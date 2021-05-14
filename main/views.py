from collections.abc import Callable

from django.shortcuts import render, redirect, get_object_or_404
from .models import Url
from .forms import UrlForm
from django.http import HttpRequest, HttpResponse
from django.views import View


class IndexView(View):
    index = 'main/index.html'
    result = 'main/result.html'

    def get(self, request: HttpRequest):
        return render(request, self.index, {'form': UrlForm()})

    def post(self, request: HttpRequest):
        if 'main' in request.POST:
            return redirect('/')

        form = UrlForm(request.POST)
        if not form.is_valid():
            context = {
                'form': UrlForm(),
                'error': f'Ошибка: '
                         f'возможно Вы ввели несуществующую ссылку или такое имя новой ссылки уже существует! '
                         f'Введите другое имя для ссылки.'
            }
            return render(request, self.index, context)

        saved_form = form.save()
        n_link = f'{saved_form.new}'
        new_link = f'{request.get_host()}/{n_link}'
        return render(request, self.result, {'tasks': new_link, 'links': n_link})


def redirect_to_main_if_post(function: Callable[[HttpRequest], HttpResponse]):
    """Декокатор, который упрощает редирект на главную страницу по методу POST"""
    def wrapper(request: HttpRequest) -> HttpResponse:
        return redirect('/') if request.method == 'POST' else function(request)
    return wrapper


@redirect_to_main_if_post
def about(request: HttpRequest): return render(request, 'main/about.html')


@redirect_to_main_if_post
def how_to_use(request: HttpRequest): return render(request, 'main/howtouse.html')


@redirect_to_main_if_post
def bot(request: HttpRequest): return render(request, 'main/bot.html')


def way(request: HttpRequest, link: str): return redirect(get_object_or_404(Url, new=link).old)
