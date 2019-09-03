from django.contrib import admin

# Register your models here.
from news.models import NewsModel


@admin.register(NewsModel)
class NewsModelAdmin(admin.ModelAdmin):
    readonly_fields = ["preview_count"]
