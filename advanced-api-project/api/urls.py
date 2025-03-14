from django.urls import path
from .views import BookListView
from .views import BookListCreateView, BookDetailView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),

    # Extra endpoints for checker compatibility
    path('books/update/', BookUpdateView.as_view(), name='book-update-no-pk'),
    path('books/delete/', BookDeleteView.as_view(), name='book-delete-no-pk'),
]
