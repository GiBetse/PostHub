from .models import dnld
from django.forms import ModelForm, TextInput, Textarea, DateInput, FileInput


class dnldForm(ModelForm):
    class Meta:
        model = dnld
        fields = ["title", "text", "img"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Звголовок'
            }),
            "text": Textarea(attrs={
                'cols': '30',
                'rows': '10',
                'class': 'form-control',
                'placeholder': 'Текст ...'
            }),
            "img": FileInput(attrs={
                'class': 'form-control',
            }),


        }
