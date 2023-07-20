from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        default="auth.User",
    )
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
        on_delete=models.PROTECT,
    )

    tag = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return self.title
