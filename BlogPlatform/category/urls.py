from django.urls import path
from .views import categories


urlpatterns = [
    path("category/", categories, name="category"),
]
