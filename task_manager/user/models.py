from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="user", blank=True, null=True)
    password = models.CharField(max_length=20)

    objects = UserManager()

    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.username
