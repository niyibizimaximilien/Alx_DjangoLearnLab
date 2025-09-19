from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# set up DRF router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # simple list view (read-only)
    path('books/', BookList.as_view(), name='book-list'),

    # router-based CRUD
    path('', include(router.urls)),
]
