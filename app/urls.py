from django.urls import path

from app import views

urlpatterns = [
    path("", views.index, name="index"),
    path("video/<str:search>", views.video, name="video"),
]
