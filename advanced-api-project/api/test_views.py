from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Book
from django.contrib.auth.models import User

class BookAPITests(APITestCase):

    def setUp(self):
        # Create a test user and authenticate
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client.login(username="testuser", password="password123")

        # Create some test books
        self.book1 = Book.objects.create(title="Book One", author="Author One", publication_year=2020)
        self.book2 = Book.objects.create(title="Book Two", author="Author Two", publication_year=2021)

        # Define endpoints
        self.list_url = reverse("book-list")
        self.detail_url = reverse("book-detail", args=[self.book1.id])

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_book_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book1.title)

    def test_create_book(self):
        data = {"title": "Book Three", "author": "Author Three", "publication_year": 2022}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book(self):
        data = {"title": "Updated Book One"}
        response = self.client.patch(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book One")

    def test_delete_book(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_year(self):
        response = self.client.get(self.list_url, {"year": 2021})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Book Two")

    def test_search_books(self):
        response = self.client.get(self.list_url, {"search": "Book"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_order_books(self):
        response = self.client.get(self.list_url, {"ordering": "title"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Book One")
