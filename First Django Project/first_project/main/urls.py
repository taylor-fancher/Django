from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('create', views.create),
    path('<int:number>', views.number),
    path('<int:number>/edit', views.edit),
    path('<int:number>/delete', views.destroy)
]
