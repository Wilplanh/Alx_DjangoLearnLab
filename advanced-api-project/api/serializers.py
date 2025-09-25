from rest_framework import serializers
from .models import Author, Book

# Serializers for Author and Book models
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

# Nested serializer for Book with embedded Author details
class NestedBookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publication_year']

# Serializer with custom validation
    def validate_publication_year(self, value):
        if value > 2025:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
