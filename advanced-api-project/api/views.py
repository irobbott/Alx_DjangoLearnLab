from rest_framework import generics
from django_filters import rest_framework as filters 
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics, permissions
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """Retrieve a list of all books with filtering, searching, and ordering."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Fields allowed for filtering
    filterset_fields = ['title', 'author__name', 'publication_year']

    # Fields allowed for searching
    search_fields = ['title', 'author__name']

    # Fields allowed for ordering
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering

# List all books or create a new book
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Allow unauthenticated users to read, but only authenticated users can create
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Retrieve, update, or delete a book by ID
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Restrict modification and deletion to authenticated users
    permission_classes = [permissions.IsAuthenticated]

# List and Create Books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# Retrieve a Single Book
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Explicitly Separate Update and Delete Views
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]