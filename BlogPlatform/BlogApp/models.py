from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        default="auth.User",
    )
    content = models.TextField()
    publication_date = models.DateField

    def __str__(self) -> str:
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name


class Comment(models.Model):
    post = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateField()

    def __str__(self) -> str:
        return self.content


class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()

    def __str__(self) -> str:
        return self.name
