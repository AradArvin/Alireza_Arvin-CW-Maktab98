from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from .models import Task
from django.views import View


class TodoOwnerRequiredMixin(View):
    model = Task
    template_name = None

    def dispatch(self, request, *args, **kwargs):
        todo = Task.objects.get(id=kwargs['pk'])
        if not todo.user == request.user:
            raise PermissionDenied
        else:
            return super().dispatch(request, *args, **kwargs)
