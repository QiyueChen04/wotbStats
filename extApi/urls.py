from django.urls import path
from . import views

urlpatterns = [
    path('', views.already_saved_extApi_response),
]
