from django.urls import path
from .views import BlogPostView, BlogCommentView, BlogCategoryView, BlogAuthorView

urlpatterns = [
    path("post/", BlogPostView.as_view(), name="post"),
    path("comment/", BlogCommentView.as_view(), name="comment"),
    path("category/", BlogCategoryView.as_view(), name="category"),
    path("author/", BlogAuthorView.as_view(), name="author"),
]
