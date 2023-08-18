from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from .models import CustomUser
from tasks.models import Task
# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email","number_of_tasks")
    list_per_page = 10
    
    def number_of_tasks(self, obj):
        num = Task.objects.filter(user=obj).count()
        return num
    
# num = Task.objects.filter(title=obj).count()