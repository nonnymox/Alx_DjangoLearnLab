# CRUD Operations for Bookshelf App

## Create a new book instance
python command:
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()

# Expected Output:
No output if successful.

## Retrieve all books
python command: 
retrieved_book = Book.objects.get(title="1984")
print(retrieved_book.title, retrieved_book.author, retrieved_book.publication_year)

# Expected Output:
1984 George Orwell 1949

## Updating its title
python command:

retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()

# Expected Output:
No output if successful.

## Deleting the book
book_to_delete = Book.objects.get(title='The Great Gatsby (Updated)')
book_to_delete.delete()  # Delete the book

# Expected Output:
(1, {'bookshelf.Book': 1})  # Indicates that one record was deleted


