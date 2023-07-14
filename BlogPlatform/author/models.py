from django.db import models
import os

# Create your models here.


class Author(models.Model):
    profile_image = models.ImageField(upload_to="author", blank=True, null=True)
    name = models.CharField(max_length=50)
    bio = models.TextField()

    def __str__(self) -> str:
        return self.name
