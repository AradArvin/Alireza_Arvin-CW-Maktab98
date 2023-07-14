from django.urls import path
from .views import BlogCategoryView


urlpatterns = [
    path("category/", BlogCategoryView.as_view(), name="category"),
]
