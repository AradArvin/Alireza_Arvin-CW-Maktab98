from django.shortcuts import render, redirect
from django.urls import reverse
from django.urls import path
from .models import Task, Category, Tag
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
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        due_date = request.POST.get("due_date")
        status = request.POST.get("status")
        category = request.POST.get("category")
        tag = request.POST.get("tag")
        Task.objects.create(
            title=title,
            description=description,
            due_date=due_date,
            status=status,
            category=category,
            tag=tag,
        )
        return redirect("all_tasks")
    else:
        task_list = Task.objects.all().order_by("-due_date")
        pagination = Paginator(task_list, 10)
        page = request.GET.get("page")
        tasks = pagination.get_page(page)
        category = Category.objects.all()
        tags = Tag.objects.all()
        context = {
            "tasks": tasks,
            "category": category,
            "tags": tags,
            "status": dict(Task.STATUS_LIST),
        }
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
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        Category.objects.create(name=name, description=description)
        return redirect("category_detail")
    else:
        category = Category.objects.all()
        return render(request, "tasks/category_detail.html", {"category": category})


def author(request):
    return render(request, "tasks/author.html")
