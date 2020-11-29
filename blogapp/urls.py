from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('author/<name>/', views.getauthor, name="author"),
    path('article/<int:id>', views.getsingle, name="single-post"),
    path('posts/<name>/', views.getcategory, name="category"),
]
