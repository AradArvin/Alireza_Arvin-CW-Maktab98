from django.db import models
from author.models import Author
from category.models import Category
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        blank=False,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=False,
    )
    content = models.TextField()
    publication_date = models.DateField

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        blank=False,
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        blank=False,
    )
    content = models.TextField()
    date = models.DateField()

    def __str__(self) -> str:
        return self.content
