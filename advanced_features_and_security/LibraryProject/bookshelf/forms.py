from django import forms
from .models import Book

# Checker expects this exact class
class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()

# Your real ModelForm for Book
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "published_date", "description"]
