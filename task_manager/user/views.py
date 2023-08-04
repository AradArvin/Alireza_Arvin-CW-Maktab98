from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginUserForm
from .models import CustomUser

# Create your views here.


def register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if not form.is_valid():
            return redirect("register")
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CreateUserForm(request.POST)
        context = {"form": form}
        return render(request, "user/register.html", context)
