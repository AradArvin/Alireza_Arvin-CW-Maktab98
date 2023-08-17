from typing import Any, Dict
from django.shortcuts import render, redirect
from django.urls import reverse
from django.urls import path
from .models import Task, Category, Tag
from django.db.models import Q
from django.core.paginator import Paginator
from .mixins import TodoOwnerRequiredMixin
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, FormView, DeleteView
# Create your views here.

class HomeView(ListView):
    model = Task
    template_name = "tasks/home.html"
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]: # research get query set method.
        context = super().get_context_data(**kwargs)
        task_list = Task.objects.filter(Q(status__contains="Ongoing"))
        pagination = Paginator(task_list, 4)
        page = self.request.GET.get("page")
        tasks = pagination.get_page(page)
        context["tasks"] = tasks
        return context
# def home(request):
#     task_list = Task.objects.filter(Q(status__contains="Ongoing"))
#     pagination = Paginator(task_list, 4)
#     page = request.GET.get("page")
#     tasks = pagination.get_page(page)
#     context = {"tasks": tasks}
#     return render(request, "tasks/home.html", context)

class AllTasksView(ListView):
    model = Task
    template_name = "tasks/all_tasks.html"
    redirect_to = "all_tasks"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        task_list = Task.objects.all().order_by("due_date")
        pagination = Paginator(task_list, 10)
        page = self.request.GET.get("page")
        tasks = pagination.get_page(page)
        category = Category.objects.all()
        tags = Tag.objects.all()
        context["tasks"] = tasks
        context["category"] = category
        context["tags"] = tags
        context["status"] = dict(Task.STATUS_LIST)
        return context
    

    def post(self, **kwargs):
        title = self.request.POST.get("title")
        description = self.request.POST.get("description")
        due_date = self.request.POST.get("due_date")
        status = self.request.POST.get("status")
        category_id = self.request.POST.get("category")
        category = Category.objects.get(pk=category_id)
        tag_s = self.request.POST.get("tag")
        tag_list = []
        for tag in tag_s:
            tag_list.append(Tag.objects.get(pk=tag))
        if self.request.POST.get("file"):
            file = self.request.POST.get("file")
            Task.objects.create(
                title=title,
                description=description,
                due_date=due_date,
                status=status,
                category=category,
                file=file,
            ).tag.set(tag_list)
            return redirect(self.redirect_to)
        Task.objects.create(
            title=title,
            description=description,
            due_date=due_date,
            status=status,
            category=category,
        ).tag.set(tag_list)
        return redirect(self.redirect_to)

# def all_tasks(request):
#     if request.method == "POST":
#         title = request.POST.get("title")
#         description = request.POST.get("description")
#         due_date = request.POST.get("due_date")
#         status = request.POST.get("status")
#         category_id = request.POST.get("category")
#         category = Category.objects.get(pk=category_id)
#         tag_s = request.POST.get("tag")
#         tag_list = []
#         for tag in tag_s:
#             tag_list.append(Tag.objects.get(pk=tag))
#         if request.POST.get("file"):
#             file = request.POST.get("file")
#             Task.objects.create(
#                 title=title,
#                 description=description,
#                 due_date=due_date,
#                 status=status,
#                 category=category,
#                 file=file,
#             ).tag.set(tag_list)
#             return redirect("all_tasks")
#         Task.objects.create(
#             title=title,
#             description=description,
#             due_date=due_date,
#             status=status,
#             category=category,
#         ).tag.set(tag_list)
#         return redirect("all_tasks")
#     else:
#         task_list = Task.objects.all().order_by("due_date")
#         pagination = Paginator(task_list, 10)
#         page = request.GET.get("page")
#         tasks = pagination.get_page(page)
#         category = Category.objects.all()
#         tags = Tag.objects.all()
#         context = {
#             "tasks": tasks,
#             "category": category,
#             "tags": tags,
#             "status": dict(Task.STATUS_LIST),
#         }
#         return render(request, "tasks/all_tasks.html", context)


class TaskDetail(TodoOwnerRequiredMixin,DetailView):
    model = Task
    template_name = "tasks/task_detail.html"
    redirect_to = "task_detail"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        category = Category.objects.all()
        tags = Tag.objects.all()
        context["category"] = category
        context["tags"] = tags
        context["status"] = dict(Task.STATUS_LIST)
        return context


    def post(self, *args, **kwargs):
        task = Task.objects.get(pk=kwargs['pk'])
        if self.request.method == "POST":
            title = self.request.POST.get("title")
            description = self.request.POST.get("description")
            due_date = self.request.POST.get("due_date")
            status = self.request.POST.get("status")
            category_id = self.request.POST.get("category")
            category = Category.objects.get(pk=category_id)
            tag_s = self.request.POST.get("tag")
            tag_list = []
            if tag_s:
                for tag in tag_s:
                    tag_list.append(Tag.objects.get(pk=tag))
            if self.request.POST.get("file"):
                file = self.request.POST.get("file")
                task.file = file
            if title:
                task.title = title
            if description:
                task.description = description
            if due_date:
                task.due_date = due_date
            if status:
                task.status = status
            if category:
                task.category = category
            if tag_list != []:
                task.tag.set(tag_list)
            task.save()
            return redirect(self.redirect_to, kwargs['pk'])
            


def search_task(request):
    return render(request, "tasks/search_task.html")

class SearchResultView(ListView):
    model = Task
    template_name = "tasks/search_task_result.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        search = self.request.GET.get("searching")
        if search:
            tasks = Task.objects.filter(
                Q(title__contains=search) | Q(tag__name__contains=search)
            ).distinct()
            context["tasks"] = tasks
        else:
            context["tasks"] = ""
        return context

# def search_task_result(request):
#     if request.method == "GET":
#         search = request.GET.get("searching")
#         if search:
#             tasks = Task.objects.filter(
#                 Q(title__contains=search) | Q(tag__name__contains=search)
#             ).distinct()
#             return render(request, "tasks/search_task_result.html", {"tasks": tasks})
#         else:
#             return render(request, "tasks/search_task_result.html", {})

class DeleteTaskView(DeleteView):
    model = Task
    success_url = "all_tasks"

# def delete_tasks(request, pk):
#     task = Task.objects.get(pk=pk)
#     task.delete()
#     return redirect("all_tasks")


def create_tag(request, pk):
    if request.method == "POST":
        tag = request.POST.get("name")
        Tag.objects.create(name=tag)
        return redirect("task_detail")


def tag_detail(request, pk):
    tag = Tag.objects.get(pk=pk)
    context = {"tag": tag}
    return render(request, "tasks/tag_detail.html", context)


def all_tags(request):
    tags = Tag.objects.all()
    context = {"tags": tags}
    return render(request, "tasks/all_tags.html", context)


def update_tag(request, pk):
    tag = Tag.objects.get(pk=pk)
    if request.method == "POST":
        name = request.POST.get("name")
        tag.name = name
        tag.save()
        return redirect("tag_detail", pk)


def category(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        if request.POST.get("image"):
            image = request.POST.get("image")
            Category.objects.create(image=image, name=name, description=description)
            return redirect("category")
        else:
            Category.objects.create(name=name, description=description)
            return redirect("category")
    else:
        categories = Category.objects.all()
        context = {"categories": categories}
        return render(request, "tasks/category.html", context)


def category_detail(request, pk):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        due_date = request.POST.get("due_date")
        status = request.POST.get("status")
        category = Category.objects.get(pk=pk)
        tag_s = request.POST.get("tag")
        tag_list = []
        for tag in tag_s:
            tag_list.append(Tag.objects.get(pk=tag))
        if request.POST.get("file"):
            file = request.POST.get("file")
            Task.objects.create(
                title=title,
                description=description,
                due_date=due_date,
                status=status,
                category=category,
                file=file,
            ).tag.set(tag_list)
            return redirect("category_detail", pk)
        else:
            Task.objects.create(
                title=title,
                description=description,
                due_date=due_date,
                status=status,
                category=category,
            ).tag.set(tag_list)
            return redirect("category_detail", pk)
    else:
        category = Category.objects.get(pk=pk)
        tags = Tag.objects.all()
        context = {
            "category": category,
            "tags": tags,
            "status": dict(Task.STATUS_LIST),
        }
        return render(request, "tasks/category_detail.html", context)


def category_update(request, pk):
    category = Category.objects.get(pk=pk)
    if request.method == "POST":
        name = request.POST.get("name2")
        description = request.POST.get("description2")
        if request.POST.get("image2"):
            image = request.POST.get("image2")
            category.image = image
        if name:
            category.name = name
        if description:
            category.description = description
        category.save()
        return redirect("category_detail", pk)


def delete_categories(request, pk):
    category = Category.objects.get(pk=pk)
    category.delete()
    return redirect("category")


def author(request):
    return render(request, "tasks/author.html")


def histories(request):
    return render(request, "tasks/histories.html")
