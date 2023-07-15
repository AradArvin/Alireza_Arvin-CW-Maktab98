from django.shortcuts import render
from .models import Author


# Create your views here.


def authors(request):
    author = Author.objects.all()
    return render(request, "author/templates/author.html", {"authors": author})


def author_detail(request, pk):
    author = Author.objects.get(pk=pk)
    return render(request, "author/templates/author_detail.html", {"author": author})
