from django.urls import path
from . import views
from .views import members

urlpatterns = [
    path('members/', views.members, name='members'),
]