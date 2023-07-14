from django.urls import path
from .views import posts, comments, post_details


urlpatterns = [
    path("post/", posts, name="post"),
    path("comment/", comments, name="comment"),
    path("post/<int:pk>/", post_details, name="post_detail"),
]
