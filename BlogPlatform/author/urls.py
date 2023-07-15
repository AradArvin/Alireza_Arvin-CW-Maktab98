from django.urls import path
from .views import authors, author_detail


urlpatterns = [
    path("author/", authors, name="author"),
    path("author/<int:pk>/", author_detail, name="author_detail"),
]
