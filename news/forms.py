from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import News


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'placeholder': 'Username kirgiziń',
            'class': 'w-full p-3 rounded-xl border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500'
        })

        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Password kirgiziń',
            'class': 'w-full p-3 rounded-xl border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500'
        })

        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Passwordtı qayta kirgiziń',
            'class': 'w-full p-3 rounded-xl border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500'
        })


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = [
            'title',
            'image',
            'category',
            'content'
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full border rounded-lg p-3'
            }),
            'category': forms.Select(attrs={
                'class': 'w-full border rounded-lg p-3'
            }),
            'content': forms.Textarea(attrs={
                'class': 'w-full border rounded-lg p-3',
                'rows': 6
            }),
        }