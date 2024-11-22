from .models import Book
from django import forms
class BookForm(forms.ModelForm):
    class Meta: 
        model = Book # tell form that model to map
        fields = ['title', 'author', 'price', 'edition']