from django.contrib import admin
from image_cropping import ImageCroppingMixin
# Register your models here.
from news.models import NewsModel


class NewsModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    readonly_fields = ["preview_count"]
    fields = [
        "image", "name", "text", "cropping", "preview_count"
    ]


admin.site.register(NewsModel, NewsModelAdmin)
