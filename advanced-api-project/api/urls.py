from django.urls import path
from .views import BookListView
from .views import BookListCreateView, BookDetailView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]
