from .models import Url
from django.forms import ModelForm, TextInput


# создание формы для ввода ссылок
class UrlForm(ModelForm):
    # параметры модели
    class Meta:
        model = Url
        # поля формы
        fields = ["old", "new"]
        widgets = {
            "old": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ссылку, которую надо сократить'
            }),
            "new": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя новой ссылки (до 20 символов) или оставьте поле пустым'
                               ' - ссылка сгенерируется автоматически',

            }),
        }
