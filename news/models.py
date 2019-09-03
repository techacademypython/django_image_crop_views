from django.db import models
from image_cropping import ImageRatioField
# Create your models here.
from django.urls import reverse


class NewsModel(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to='uploaded_images')
    name = models.CharField(max_length=200)
    text = models.TextField()

    cropping = ImageRatioField('image', '348x397')

    preview_count = models.PositiveIntegerField(default=0)

    create_date = models.DateTimeField(auto_now_add=True)

    def get_detail(self):
        return reverse("detail", kwargs={
            "pk": self.pk
        })

    def __str__(self):
        return f"{self.name}"
