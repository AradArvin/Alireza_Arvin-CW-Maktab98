from django.shortcuts import render
from .models import Author

# Create your views here.


def authors(request):
    author = Author.objects.all()
    return render(request, "author.html", {"authors": author})
