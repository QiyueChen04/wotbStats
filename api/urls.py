from django.urls import path
from . import views

urlpatterns = [
    path('allTanks/', views.getAllTanks),
    path('tankInfo/', views.getTankInfo),
]
