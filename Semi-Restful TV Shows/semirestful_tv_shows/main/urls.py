from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/<int:id>', views.one_show),
    path('shows/<int:id>/edit', views.edit_show),
    path('shows/<int:id>/update', views.update),
    path('shows/<int:id>/destroy', views.delete_show),
    path('new', views.add_show),
    path('create', views.create)
]