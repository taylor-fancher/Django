from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('books', views.books),
    path('authors', views.authors),
    path('create_book', views.create_book),
    path('book/<int:number>', views.this_book),
    path('create_author', views.create_author),
    path('author/<int:number>', views.this_author)
]
