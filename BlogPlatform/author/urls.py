from django.urls import path
from .views import authors


urlpatterns = [
    path("author/", authors, name="author"),
]
