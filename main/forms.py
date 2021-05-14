from django.forms import ModelForm, TextInput

from .models import Url


class UrlForm(ModelForm):
    class Meta:
        model = Url
        fields = ("old", "new")
        widgets = {
            "old": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ссылку, которую надо сократить'
            }),
            "new": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя новой ссылки (до 20 символов) '
                               'или оставьте поле пустым - ссылка сгенерируется автоматически',
            }),
        }
