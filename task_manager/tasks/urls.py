from django.urls import path
from .views import *


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("author/", author, name="author"),
    path("task/", AllTasksView.as_view(), name="all_tasks"),
    path("task/<int:pk>/", TaskDetail.as_view(), name="task_detail"),
    path("search/", search_task, name="search_task"),
    path("search_result/", SearchResultView.as_view(), name="search_task_result"),
    path("deltask/<int:pk>/", DeleteTaskView.as_view(), name="delete_tasks"),
    path("category/", category, name="category"),
    path("category/<int:pk>/", category_detail, name="category_detail"),
    path("category-update/<int:pk>/", category_update, name="category_update"),
    path("delcat/<int:pk>/", delete_categories, name="delete_categories"),
    path("ctag/<int:pk>/", CreateTagView.as_view(), name="create_tag"),
    path("tag/<int:pk>/", tag_detail, name="tag_detail"),
    path("tag/", all_tags, name="all_tags"),
    path("utag/<int:pk>/", update_tag, name="update_tag"),
    path("History/", histories, name="Histories"),
]
