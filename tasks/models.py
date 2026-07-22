from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["is_done", "-datetime"]

    def __str__(self):
        return self.content[:50]

    @property
    def is_overdue(self):
        return (
            bool(self.deadline) and not self.is_done and self.deadline < timezone.now()
        )
