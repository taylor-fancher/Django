from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('register', views.register),
    path('new_user', views.new_user),
    path('dashboard', views.dashboard),
    path('add_book_with_review', views.add_book_review),
    path('create_book_review', views.create_book_review),
    path('book/<int:id>', views.one_book),
    path('add_review', views.add_review),
]