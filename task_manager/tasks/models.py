from django.db import models
from user.models import CustomUser

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to="category/", blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    due_date = models.DateTimeField()

    STATUS_LIST = [
        ("Ongoing", "Ongoing"),
        ("Done", "Done"),
        ("Cancelled", "Cancelled"),
    ]

    status = models.CharField(
        max_length=10,
        choices=STATUS_LIST,
        default="Ongoing",
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
    )

    tag = models.ManyToManyField(Tag)
    file = models.FileField(upload_to="taskfile/", blank=True, null=True)
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return self.title
