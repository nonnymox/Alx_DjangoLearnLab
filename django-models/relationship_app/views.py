
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, HttpResponse
# Create your views here.

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect

# Custom Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')  # Redirect to a suitable page after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Django's built-in LoginView and LogoutView will handle login and logout automatically


def list_books(request):
    books = Book.objects.all()  # Retrieve all books
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return HttpResponse("Welcome, Admin!")

@user_passes_test(is_librarian)
def librarian_view(request):
    return HttpResponse("Welcome, Librarian!")

@user_passes_test(is_member)
def member_view(request):
    return HttpResponse("Welcome, Member!")
