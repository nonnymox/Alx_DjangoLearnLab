from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# ListView: Retrieve all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Open to all users
    def get_queryset(self):
        queryset = Book.objects.all()
        year = self.request.query_params.get('year')
        if year:
            queryset = queryset.filter(publication_year=year)
        return queryset

# DetailView: Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Open to all users

# CreateView: Add a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Authenticated users only

# UpdateView: Modify an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Authenticated users only

# DeleteView: Remove a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Authenticated users only

# BookListView: Handles GET requests to retrieve all books.
# BookDetailView: Handles GET requests to retrieve a single book by ID.
# BookCreateView: Handles POST requests to create a new book (Authenticated users only).
# BookUpdateView: Handles PUT/PATCH requests to update an existing book (Authenticated users only).
# BookDeleteView: Handles DELETE requests to remove a book (Authenticated users only).
