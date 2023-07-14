from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Comment


# Create your views here.
class BlogPostView(ListView):
    model = Post
    template_name = "post.html"


class BlogCommentView(DetailView):
    model = Comment
    template_name = "comment.html"
