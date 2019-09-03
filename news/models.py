from django.db import models


# Create your models here.
from django.urls import reverse


class NewsModel(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()

    preview_count = models.PositiveIntegerField(default=0)

    create_date = models.DateTimeField(auto_now_add=True)

    def get_detail(self):
        return reverse("detail", kwargs={
            "pk": self.pk
        })

    def __str__(self):
        return f"{self.name}"

