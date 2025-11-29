from rest_framework import generics
from .models import Book
from .serializers import BookSerializer


class BookList(generics.ListAPIView):
    """API endpoint that returns a list of all books."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
