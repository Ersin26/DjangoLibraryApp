from apps.library.api.views import create_book, create_borrow
from django.urls import path

urlpatterns = [
    path('book/create/', create_book),
    path('borrow/create/', create_borrow)
]
