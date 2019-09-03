from django.urls import path
from news import views

urlpatterns = [
    path("", views.MainIndex.as_view(), name="main"),
    path("news/<int:pk>/", views.NewsDetail.as_view(), name="detail"),
]
