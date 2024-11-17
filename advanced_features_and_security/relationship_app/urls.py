from django.urls import path
from . import views
from .views import list_books
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Book management
    path('books/', list_books, name='list_books'),  # Function-based view
    path('books/add/', views.add_book, name='add_book/'),  # Add book
    path('books/edit/<int:pk>/', views.edit_book, name='edit_book/'),  # Edit book
    path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),  # Delete book
    
    # Library detail (class-based view)
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    
    # Authentication
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    
    # Role-based views
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
]
