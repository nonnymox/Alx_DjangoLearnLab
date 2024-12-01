from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)  # Author's name

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)  # Book title
    publication_year = models.PositiveIntegerField()  # Year published
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')  # Link to Author

    def __str__(self):
        return self.title
# Models for Author and Book.
# Author has a one-to-many relationship with Book.
