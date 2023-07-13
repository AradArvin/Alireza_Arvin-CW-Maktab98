from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Comment, Author, Category


# Create your views here.
class BlogPostView(ListView):
    model = Post
    template_name = "post.html"


class BlogCommentView(DetailView):
    model = Comment
    template_name = "comment.html"


class BlogCategoryView(DetailView):
    model = Category
    template_name = "category.html"


class BlogAuthorView(DetailView):
    model = Author
    template_name = "author.html"
