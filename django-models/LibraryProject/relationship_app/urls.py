from django.urls import path
from .views import list_books, LibraryDetailView, user_login, user_logout, register
from .views import list_books, LibraryDetailView, register

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', register, name='register'),  # Ensure this line is included
]
