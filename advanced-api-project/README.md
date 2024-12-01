# Advanced API Project

## Overview
This project demonstrates how to use Django REST Framework to handle CRUD operations efficiently with generic views.

## API Endpoints
- `GET /api/books/`: List all books.
- `GET /api/books/<int:pk>/`: Retrieve a book by ID.
- `POST /api/books/create/`: Create a new book (Authenticated users only).
- `PUT /api/books/<int:pk>/update/`: Update an existing book (Authenticated users only).
- `DELETE /api/books/<int:pk>/delete/`: Delete a book (Authenticated users only).

## Permissions
- List and Detail views: Accessible to all users.
- Create, Update, and Delete views: Restricted to authenticated users.
