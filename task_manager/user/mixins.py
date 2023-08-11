from django.core.exceptions import PermissionDenied
from .models import CustomUser



class ProfileMixin:

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if not user == request.user:
            raise PermissionDenied
        else:
            return super().dispatch(request, *args, **kwargs)
