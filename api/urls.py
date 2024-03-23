from django.urls import path
from . import views

urlpatterns = [
    path('getAllTanks/', views.getAllTanks),
    path('getTankInfo/', views.getTank),
    path('getTankGuns/', views.getTankGuns),
]
