from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CreateUserForm, LoginUserForm
from .auth import CustomeEmailBack
from django.views import View
from .mixins import ProfileMixin
from .models import CustomUser
# Create your views here.


def register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if not form.is_valid():
            return redirect("register")
        if form.is_valid():
            user = form.save(commit=False)
            password = user.password
            user.set_password(password)
            form.save()
            return redirect("home")
    else:
        form = CreateUserForm()
        context = {"form": form}
        return render(request, "user/register.html", context)


def logging(request):
    if request.method == "POST":
        form = LoginUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            auth = authenticate(request=request, username=username, password=password)
            print(auth)
            if auth is not None:
                login(request, auth)
                return redirect("home")
            else:
                return redirect("login")
        else:
            return redirect("login")
    else:
        form = LoginUserForm()
        context = {"form": form}
        return render(request, "user/login.html", context)


class ProfileView(ProfileMixin, View):
    template_name = "user/profile.html"
    form_class = CreateUserForm
    redirect_to = "profile_detail"
    def get(self, request, *args, **kwargs):
        user = CustomUser.objects.get(pk=kwargs['pk'])
        form = self.form_class()
        context = {"user":user, "form":form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        user = CustomUser.objects.get(pk=kwargs['pk'])
        form = self.form_class(request.POST, instance=user)
        if form.is_valid():
            user.save()
            return redirect(self.redirect_to)
        context = {"user":user}
        return render(request, self.template_name, context)