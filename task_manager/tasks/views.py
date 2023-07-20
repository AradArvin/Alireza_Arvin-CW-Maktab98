from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Task, Category
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.


def home(request):
    task_list = Task.objects.filter(Q(status__contains="Ongoing"))
    pagination = Paginator(task_list, 2)
    page = request.GET.get("page")
    tasks = pagination.get_page(page)
    context = {"tasks": tasks}
    return render(request, "tasks/home.html", context)


def all_tasks(request):
    task_list = Task.objects.all().order_by("-due_date")
    pagination = Paginator(task_list, 10)
    page = request.GET.get("page")
    tasks = pagination.get_page(page)
    context = {"tasks": tasks}
    return render(request, "tasks/all_tasks.html", context)


def task_detail(request, pk):
    task = Task.objects.get(pk=pk)
    return render(request, "tasks/task_detail.html", {"task": task})


def search_task(request):
    return render(request, "tasks/search_task.html")


def search_task_result(request):
    if request.method == "GET":
        search = request.GET.get("searching")
        if search:
            tasks = Task.objects.filter(
                Q(title__contains=search) | Q(tag__name__contains=search)
            ).distinct()
            return render(request, "tasks/search_task_result.html", {"tasks": tasks})
        else:
            return render(request, "tasks/search_task_result.html", {})


def category_detail(request):
    category = Category.objects.all()
    return render(request, "tasks/category_detail.html", {"category": category})


def author(request):
    return render(request, "tasks/author.html")
