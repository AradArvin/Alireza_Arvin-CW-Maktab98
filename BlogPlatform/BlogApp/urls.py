from django.urls import path
from .views import BlogPostView, BlogCommentView, BlogDetailView

urlpatterns = [
    path("post/", BlogPostView.as_view(), name="post"),
    path("comment/", BlogCommentView.as_view(), name="comment"),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
]
