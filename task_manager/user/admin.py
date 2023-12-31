from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from .models import CustomUser
from tasks.models import Task
from django.db.models import Count

# Register your models here.


class GreatFilter(admin.SimpleListFilter):
    title = "is_great"
    parameter_name = "great"

    def lookups(self, request, modeladmin):
        return [
            ("great", "is great"),
            ("not_great", "not great"),
        ]
    
    def queryset(self, request, queryset):
        if self.value() == "great":
            return queryset.filter(number_of_tasks__gt=10).distinct()
        
        if self.value() == "not_great":
            return queryset.filter(number_of_tasks__lt=10).distinct()

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        queryst = super().get_queryset(request)
        queryst = queryst.annotate(number_of_tasks=Count("task"))
        return queryst

    def number_of_tasks(self, obj):
        num = obj.number_of_tasks
        return num
    
    
    list_display = ("username", "email","number_of_tasks")
    number_of_tasks.admin_order_field = "number_of_tasks"
    list_filter = (GreatFilter,)
    list_per_page = 10
    readonly_fields = ['image_tag']
    
# num = Task.objects.filter(user=obj).count()

