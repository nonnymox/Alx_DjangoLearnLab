from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Fields to display
    search_fields = ('title', 'author')  # Fields to search
    list_filter = ('publication_year',)  # Filter by publication year

# Register model with custom admin class
admin.site.register(Book, BookAdmin)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            None,
            {
                'fields': ('date_of_birth', 'profile_photo'),
            },
        ),
    )
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            None,
            {
                'fields': ('date_of_birth', 'profile_photo'),
            },
        ),
    )
    list_display = ('username', 'email', 'date_of_birth', 'is_staff', 'is_active')

admin.site.register(CustomUser, CustomUserAdmin)