from django.urls import path

from . import views  # import views from the current dir

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("", views.home, name="home")
]

