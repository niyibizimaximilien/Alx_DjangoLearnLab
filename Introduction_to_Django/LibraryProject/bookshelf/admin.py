from django.contrib import admin
from .models import Book

# Customize the admin interface for Book
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to show
    search_fields = ('title', 'author')                     # Add search bar
    list_filter = ('publication_year',)                     # Add filters

# Register the Book model with the custom admin
admin.site.register(Book, BookAdmin)
