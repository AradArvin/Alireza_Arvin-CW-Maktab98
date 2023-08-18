from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.html import mark_safe

# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="user", blank=True, null=True)
    password = models.CharField(max_length=20)

    objects = UserManager()

    REQUIRED_FIELDS = []

    def image_tag(self):
        return mark_safe('<img src="user/%s" width="150" height="150" />' % (self.image))

    image_tag.short_description = 'Image'

    def __str__(self) -> str:
        return self.username
