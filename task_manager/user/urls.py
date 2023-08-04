from django.urls import path

from .views import register, logging

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", logging, name="login"),
]
