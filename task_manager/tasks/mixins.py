from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from .models import Task



class TodoOwnerRequiredMixin:

    def dispatch(self, request, *args, **kwargs):
        task = Task.objects.get(id=kwargs['pk'])
        if not task.user == request.user:
            raise PermissionDenied
        else:
            return super().dispatch(request, *args, **kwargs)
