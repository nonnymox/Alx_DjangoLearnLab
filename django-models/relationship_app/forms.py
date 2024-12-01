from django import forms
from .models import Book  # Make sure this matches your model's import

class BookForm(forms.ModelForm):
    class Meta:
        model = Book  # The model the form is for
        fields = ['title', 'author', 'publication_date']  # List the fields you want to include in the form