from django.core import validators
from django import forms
from .models import Books

class BookRegister(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['author_name', 'book_name']
        widgets = {
            'author_name': forms.TextInput(attrs={'class': 'form-control'}),
            'book_name': forms.TextInput(attrs={'class': 'form-control'}),
        }