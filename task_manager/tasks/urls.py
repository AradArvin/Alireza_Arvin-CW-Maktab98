from django.urls import path
from .views import (
    home,
    author,
    all_tasks,
    task_detail,
    search_task,
    search_task_result,
    category,
    category_detail,
    category_update,
    create_tag,
    tag_detail,
    all_tags,
    update_tag,
)


urlpatterns = [
    path("", home, name="home"),
    path("author/", author, name="author"),
    path("task/", all_tasks, name="all_tasks"),
    path("task/<int:pk>/", task_detail, name="task_detail"),
    path("search/", search_task, name="search_task"),
    path("search_result/", search_task_result, name="search_task_result"),
    path("category/", category, name="category"),
    path("category/<int:pk>/", category_detail, name="category_detail"),
    path("category-update/<int:pk>/", category_update, name="category_update"),
    path("ctag/<int:pk>/", create_tag, name="create_tag"),
    path("tag/<int:pk>/", tag_detail, name="tag_detail"),
    path("tag/", all_tags, name="all_tags"),
    path("utag/<int:pk>/", update_tag, name="update_tag"),
]
