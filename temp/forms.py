from django.forms import ModelForm, TextInput, Textarea
from .models import Articles


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'review_text']

        widgets = {
            'title': TextInput(attrs={
                'placeholder': 'Название статьи'
            }),
            'review_text': Textarea(attrs={
                'placeholder': 'Текст статьи'
            })
        }