from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return [book.title for book in books]

# 2. List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return [book.title for book in books]

# 3. Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian  # Use the related_name if you set one in the OneToOneField
    return librarian.name if librarian else "No librarian assigned"

# Sample usage
if __name__ == "__main__":
    # Replace 'Author Name' and 'Library Name' with actual names in your database
    print("Books by a specific author:", get_books_by_author("Author Name"))
    print("Books in the library:", get_books_in_library("Library Name"))
    print("Librarian for the library:", get_librarian_for_library("Library Name"))
