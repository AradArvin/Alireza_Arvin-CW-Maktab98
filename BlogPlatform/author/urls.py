from django.urls import path
from .views import BlogAuthorView


urlpatterns = [
    path("author/", BlogAuthorView.as_view(), name="author"),
]
