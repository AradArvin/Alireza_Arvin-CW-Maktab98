from django.shortcuts import render
from .models import Post, Comment, Category


# Create your views here.


def posts(request):
    posts = Post.objects.all()
    return render(request, "BlogApp/templates/post.html", {"posts": posts})


def comments(request):
    comment = Comment.objects.all()
    return render(request, "comment.html", {"comments": comment})


def post_details(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    return render(
        request,
        "BlogApp/templates/post_detail.html",
        {"post": post, "comments": comments},
    )


def categories(request):
    category = Category.objects.all()
    return render(request, "BlogApp/templates/category.html", {"categories": category})
