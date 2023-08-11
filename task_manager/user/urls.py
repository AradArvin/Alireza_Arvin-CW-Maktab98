from django.urls import path

from .views import register, logging, ProfileView

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", logging, name="login"),
    path("profile/", ProfileView.as_view(), name="profile"),
]
