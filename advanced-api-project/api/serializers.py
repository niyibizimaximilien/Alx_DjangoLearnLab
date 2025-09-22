from rest_framework import serializers
from .models import Author, Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    Validates that the publication_year is not in the future.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """
        Ensure the publication year is not in the future.
        """
        if value > date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    Includes nested BookSerializer for the related books.
    """
    books = BookSerializer(many=True, read_only=True)  # Nested serialization

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
