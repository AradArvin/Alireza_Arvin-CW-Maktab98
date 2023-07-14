from django.urls import path
from .views import BlogPostView, BlogCommentView

urlpatterns = [
    path("post/", BlogPostView.as_view(), name="post"),
    path("comment/", BlogCommentView.as_view(), name="comment"),
]
