from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITests(APITestCase):
    """
    Test cases for Book API endpoints.
    """

    def setUp(self):
        """
        Set up test data and authentication.
        """
        # Create a test user and authenticate
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        # Create an author
        self.author = Author.objects.create(name="John Doe")

        # Create books
        self.book1 = Book.objects.create(
            title="Book One",
            publication_year=2020,
            author=self.author
        )
        self.book2 = Book.objects.create(
            title="Book Two",
            publication_year=2022,
            author=self.author
        )

        # Endpoints
        self.list_url = "/books/"
        self.detail_url = f"/books/{self.book1.id}/"

    def test_list_books(self):
        """
        Test retrieving a list of all books.
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['title'], self.book1.title)

    def test_filter_books_by_year(self):
        """
        Test filtering books by publication year.
        """
        response = self.client.get(self.list_url, {'year': 2020})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Book One")

    def test_retrieve_book_detail(self):
        """
        Test retrieving the details of a single book.
        """
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_create_book(self):
        """
        Test creating a new book.
        """
        data = {
            "title": "Book Three",
            "publication_year": 2024,
            "author": self.author.id
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book(self):
        """
        Test updating an existing book.
        """
        data = {
            "title": "Updated Book One",
            "publication_year": 2021,
            "author": self.author.id
        }
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book One")

    def test_delete_book(self):
        """
        Test deleting a book.
        """
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_unauthorized_access(self):
        """
        Test that unauthorized users cannot perform restricted actions.
        """
        self.client.logout()
        response = self.client.post(self.list_url, {
            "title": "Unauthorized Book",
            "publication_year": 2024,
            "author": self.author.id
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

