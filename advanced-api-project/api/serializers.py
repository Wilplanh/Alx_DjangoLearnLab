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
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date']

# Serializer with custom validation
    def validate_published_date(self, value):
        if value.year > 2025:
            raise serializers.ValidationError("Published date cannot be in the future.")
        return value
