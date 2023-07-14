from django.shortcuts import render
from django.views.generic import ListView
from .models import Category


# Create your views here.
class BlogCategoryView(ListView):
    model = Category
    template_name = "category.html"
