from .models import Author, Book, Library, Librarian

# List all books in a library.
def list_books_in_library(library):
    return library.books.all()

# Query all books by a specific author.
def get_books_by_author(author):
    return Book.objects.filter(author=author)

# Retrieve the librarian for a library.
def get_librarian_for_library(library):
    return Librarian.objects.get(library=library)
