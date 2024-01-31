from django.urls import path
from . import views

urlpatterns = [
    path("/<str:tank_name1>/<str:tank_name2>", views.compare, name = ""),
]