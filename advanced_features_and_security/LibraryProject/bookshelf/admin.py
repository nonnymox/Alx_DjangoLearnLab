from django.contrib import admin

# Register your models here.
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Fields to display
    search_fields = ('title', 'author')  # Fields to search
    list_filter = ('publication_year',)  # Filter by publication year

# Register model with custom admin class
admin.site.register(Book, BookAdmin)
