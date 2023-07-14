from django.db import models
from author.models import Author
from category.models import Category


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        default=Author,
        blank=False,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
    content = models.TextField()
    publication_date = models.DateField

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    post = models.CharField(max_length=100)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        default=Author,
        blank=False,
    )
    content = models.TextField()
    date = models.DateField()

    def __str__(self) -> str:
        return self.content
